from matplotlib import pyplot as plt
import numpy as np
import os
import shutil
from tqdm import tqdm
import copy

from .aero import Aero
from .geometry import Plane, Section


class Dihedral():
    def __init__(self, dihedral_config_file: str, aero_config_file: str):

        #   Clean temp folders.
        self.path = os.path.split(dihedral_config_file)[0]

        try:
            if os.path.isdir(self.path+"/results") == True:
                shutil.rmtree(self.path+"/results")
            if os.path.isdir(self.path+"/generated planes") == True:
                shutil.rmtree(self.path+"/generated planes")
            if os.path.isdir(self.path+"/cases") == True:
                shutil.rmtree(self.path+"/cases")
        except PermissionError:
            raise PermissionError("Close all results, geometry, case files")

        os.mkdir(self.path+"/generated planes")
        os.mkdir(self.path+"/results")
        os.mkdir(self.path+"/cases")

        if os.path.exists(f"{self.path}/avl.exe") == False:
            print("\u001b[31m[Error]\u001b[0m avl.exe not found.")
            exit()

        self.read_config(dihedral_config_file)
        self.aero_config_file = aero_config_file

        return None

    def read_config(self, config_file):
        """
        Reads dihedral config file.

        Arguments:
            config_file: {string} -- Dihedral config file.
        """
        def str_to_bool(x): return True if (x == "Y") else False

        with open(config_file, 'r') as f:
            lines = f.readlines()
        lines = [line for line in lines if line[0]
                 != "#" and line != "\n"]  # cleans input

        if lines[0].strip() != "DIHEDRAL CONFIG":
            print(
                f"\u001b[31m[Error]\u001b[0m Wrong config file type ({config_file}).")
            exit()

        lines = lines[1:]

        self.plane_file = lines[0].split(": ")[1:][0].strip()
        self.wing_aerofoil = lines[1].split(": ")[1:][0]
        self.elevator_aerofoil = lines[2].split(": ")[1:][0]
        self.fin_aerofoil = lines[3].split(": ")[1:][0]
        self.angle_min = float(lines[4].split()[1])
        self.angle_max = float(lines[5].split()[1])
        self.increment = int(lines[6].split()[1])
        self.span_loc = float(lines[7].split()[1])
        self.threads = float(lines[8].split()[1])
        self.show_geom_plt = str_to_bool(lines[9].split(": ")[1][0])

        return None

    def generate_planes(self):
        """
        Generates tail configurations, saves as AVL readable plane files.

        Returns:
            planes {list[Plane]} -- List of plane objects with modified geometry.
        """
        #   Generate reference plane goemetry. Strips wing section to be modified and removes fin.
        self.ref_plane = Plane(name="REF")
        self.ref_plane.read(self.plane_file)
        self.ref_plane.strip_section("Main Wing")
        self.ref_plane.strip_surface("Fin")

        planes = []

        mac = self.ref_plane.mac
        span = self.ref_plane.b_w
        # Half span (AVL wings are defined from centreline to outboard.)
        hspan = span/2

        count = 0
        theta_range = np.linspace(  # Dihedral angle range.
            self.angle_min,
            self.angle_max,
            int(1+(self.angle_max-self.angle_min)/self.increment)
        )
        for theta in theta_range:
            name = str(count)

            plane = Plane(name=name)
            plane.dihedral_angle = theta
            plane.dihedral_split = self.span_loc

            # Location to split wing for dihedral start.
            split_loc = hspan*self.span_loc/100
            plane.dihedral_splitY = split_loc
            plane.span = span

            # Copy required because reasons.
            mod_geom = copy.copy(self.ref_plane.file_str)

            # Calculates tip Z due to dihedral angle
            Zle = round((hspan-split_loc)*np.sin(np.radians(theta)), 3)
            plane.tipZ = Zle
            # Calcualtes tip Y due to dihedral angle
            Yle = round((hspan-split_loc) *
                        np.cos(np.radians(theta))+split_loc, 3)
            plane.tipY = Yle

            #   Generate root, split and tip sections in AVL format.
            root = Section(self.ref_plane.Xle, 0, 0, mac, int(
                split_loc*0.02), -2, self.elevator_aerofoil)
            split = Section(self.ref_plane.Xle, split_loc, 0, mac, int(
                (np.sqrt(Yle**2+Zle**2)-split_loc)*0.02), -1, self.elevator_aerofoil)
            # Creates tip section based off tip geometry
            tip = Section(self.ref_plane.Xle, Yle, Zle,
                          mac, 0, 0, self.elevator_aerofoil)

            mod_str = str(root)  # Gets section string
            mod_str += str(split)
            mod_str += str(tip)

            for index, line in enumerate(mod_geom):
                if line == "MARKER\n":  # Finds marker
                    mod_geom.pop(index)  # Removes marker
                    # Inserts modified sections
                    mod_geom.insert(index, mod_str)

            #   Writes plane file.
            file_name = name = f"{plane.name}-{theta}deg-{self.span_loc}%"
            plane.geom_file = f"{self.path}/generated planes/{file_name}.avl"
            with open(plane.geom_file, 'w') as file:
                file.write("".join(mod_geom))
            count += 1

            planes.append(plane)

        self.planes = planes

        return planes

    def run(self):
        """
        Runs aero analysis.
        """
        aero = Aero(self.aero_config_file)  # initialises aero analysis, reads config file.
        if aero.polars == False:
            raise ValueError("Polars must be enabled for dihedral analysis.")

        #   Can't do multithreaded analysis without some thinking and extra code :(
        for plane in tqdm(self.planes, desc="Aero analysis"):
            aero.run(plane)

        return None

    def plot(self):
        """
        Main plot function. Handles polar and eigenmode plots in subplots.
        """
        fig, (ax1, ax2, ax3) = plt.subplots(
            ncols=3, figsize=(12, 3), sharex=True)

        polar_plt = self.plot_polars(ax1, ax2, ax3)
        # mode_plt=self.plot_modes(ax4)

        plt.tight_layout()

        if self.plot_dihedral_angle == True:
            geom_plt = self.plot_dihedral_angle()

        plt.show()

        return None

    def plot_polars(self, ax1, ax2, ax3):
        """
        Draws polar plots.

        Arguments:
            ax1, ax2, ax3 {matplotlib.Axes} -- Subplot axes.

        Returns:
            plt {matplotlib.pyplot}
        """
        dihedral_angles = [plane.dihedral_angle for plane in self.planes]

        #   Aero polar plot
        Cl_0 = self.planes[0].polars['Cl'].iloc[-1]
        Cd_0 = self.planes[0].polars['Cd'].iloc[-1]
        Cl_delta = [100*(plane.polars['Cl'].iloc[-1]-Cl_0) /
                    Cl_0 for plane in self.planes]
        Cd_delta = [100*(plane.polars['Cd'].iloc[-1]-Cd_0) /
                    Cd_0 for plane in self.planes]

        ax1.plot(dihedral_angles, Cl_delta, label="Lift ($C_{L}$)")
        ax1.plot(dihedral_angles, Cd_delta, label="Lift ($C_{D}$)")

        ax1.set_ylabel(
            f"\u0394 (%) @ {self.planes[0].polars['Alpha (deg)'].iloc[-1]}\u00B0 AoA")
        ax1.legend(loc='upper left')
        ax1.set_title("Aero Coeffients")

        #   Stability derivative plot.
        Clb = [plane.polars['Clb'].iloc[0] for plane in self.planes]
        Clp = [plane.polars['Clp'].iloc[0] for plane in self.planes]

        ax2.plot(dihedral_angles, Clb, label="Dihedral ($Cl_{b}$)")
        ax2.plot(dihedral_angles, Clp, label="Roll Rate ($Cl_{p}$)")

        ax2.legend()
        ax2.set_title("Stability Derivatives")
        ax2.set_ylabel("Dervative [NA]")
        ax2.set_xlabel(
            f"Dihedral Angle (\u00B0) - Split Location={self.planes[0].dihedral_split}% of Span")

        #   Spiral stability plot
        spiral = [plane.polars['spiral'].iloc[1] for plane in self.planes]

        ax3.plot(dihedral_angles, spiral)
        ax3.set_title("Spiral Stability (>1 = stable)")
        # ax3.set_xlabel(f"Dihedral Angle (\u00B0) - Split Location={self.planes[0].dihedral_split}% of Span")
        ax3.set_ylabel("Clb.Cnr / Clr.Cnb [NA]")

        return plt

    def plot_modes(self, ax4):
        """
        Draws eigenmode plot.

        Arguments:
            ax4 {matplotlib.Axes} -- Subplot axes.

        Returns:
            plt {matplotlib.pyplot}
        """
        dihedral_angles = [plane.dihedral_angle for plane in self.planes]

        roll_0 = self.planes[0].modes["roll"][0][0]
        dutch_0 = self.planes[0].modes["dutch"][0][0]
        roll_delta = [100*(plane.modes["roll"][0][0]-roll_0) /
                      roll_0 for plane in self.planes]
        dutch_delta = [100*(plane.modes["dutch"][0][0] -
                            dutch_0)/dutch_0 for plane in self.planes]

        ax4.set_xlabel(
            f"Dihedral Angle (\u00B0) - Split Location={self.planes[0].dihedral_split}% of Span")
        ax4.set_ylabel("\u0394 Damping (%)")
        ax4.set_title("Eigenmode Damping")

        ax4.plot(dihedral_angles, roll_delta, label="Roll")
        ax4.plot(dihedral_angles, dutch_delta, label="Dutch Roll")
        ax4.legend()

        return

    def plot_dihedral_angle(self):
        """
        Draws spanwise dihedral geometry plot.

        Returns:
            plt {matplotlib.pyplot}
        """
        plt.figure()
        plt.title("Spanwise Geometry Plot")

        plt.xlabel("Y (mm)")
        plt.ylabel("Z (mm)")
        plt.xlim(0, max([plane.tipY for plane in self.planes]))
        plt.ylim(0, max([plane.tipY for plane in self.planes]))

        for plane in self.planes:
            plt.plot([0, plane.dihedral_splitY, plane.tipY],
                     [0, 0, plane.tipZ])

        return plt


if __name__ == "__main__":
    dihedral = Dihedral('dihedral.config', 'aero.config')
    dihedral.generate_planes()
    dihedral.run()
    dihedral.plot()
