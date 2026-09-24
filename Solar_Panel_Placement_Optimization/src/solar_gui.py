import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import math


class SolarPanelApp:

    def __init__(self, root):

        self.root = root

        self.root.title(
            "Solar Panel Placement Optimization"
        )

        # MEDIUM WINDOW
        self.root.geometry("980x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#F4F7FB")

        # =========================
        # COLORS
        # =========================

        self.NAVY = "#102A43"
        self.DARK_BLUE = "#173B63"
        self.BLUE = "#2563EB"
        self.LIGHT_BLUE = "#EFF6FF"

        self.GREEN = "#16A34A"
        self.LIGHT_GREEN = "#ECFDF5"

        self.PURPLE = "#7C3AED"
        self.LIGHT_PURPLE = "#F5F3FF"

        self.ORANGE = "#F59E0B"
        self.RED = "#DC2626"

        self.WHITE = "#FFFFFF"
        self.BACKGROUND = "#F4F7FB"

        self.TEXT = "#243B53"
        self.MUTED = "#6B7280"
        self.BORDER = "#D9E2EC"

        # =========================
        # VARIABLES
        # =========================

        self.entries = []

        # =========================
        # CREATE UI
        # =========================

        self.create_sidebar()
        self.create_main_area()
        self.create_header()
        self.create_banner()
        self.create_workspace()

    # =========================================================
    # SIDEBAR
    # =========================================================

    def create_sidebar(self):

        self.sidebar = tk.Frame(
            self.root,
            bg=self.NAVY,
            width=190
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        self.sidebar.pack_propagate(False)

        # LOGO
        tk.Label(
            self.sidebar,
            text="SOLAR",
            font=("Arial", 22, "bold"),
            bg=self.NAVY,
            fg="#FACC15"
        ).pack(
            anchor="w",
            padx=22,
            pady=(25, 0)
        )

        tk.Label(
            self.sidebar,
            text="OPTIMIZER",
            font=("Arial", 17, "bold"),
            bg=self.NAVY,
            fg="white"
        ).pack(
            anchor="w",
            padx=22
        )

        tk.Label(
            self.sidebar,
            text="DAA MINI PROJECT",
            font=("Arial", 8, "bold"),
            bg=self.NAVY,
            fg="#9FB3C8"
        ).pack(
            anchor="w",
            padx=22,
            pady=(3, 22)
        )

        # NAVIGATION BUTTONS

        self.sidebar_item(
            "Dashboard",
            self.show_dashboard,
            True
        )

        self.sidebar_item(
            "Greedy Algorithm",
            self.show_greedy,
            False
        )

        self.sidebar_item(
            "Energy Analysis",
            self.show_energy,
            False
        )

        self.sidebar_item(
            "Optimization",
            self.show_optimization,
            False
        )

        # LINE

        tk.Frame(
            self.sidebar,
            bg="#29445E",
            height=1
        ).pack(
            fill="x",
            padx=22,
            pady=20
        )

        # PROJECT DETAILS

        tk.Label(
            self.sidebar,
            text="PROJECT DETAILS",
            font=("Arial", 8, "bold"),
            bg=self.NAVY,
            fg="#829AB1"
        ).pack(
            anchor="w",
            padx=22
        )

        tk.Label(
            self.sidebar,
            text="Design & Analysis\nof Algorithms",
            font=("Arial", 9),
            bg=self.NAVY,
            fg="#D9E2EC",
            justify="left"
        ).pack(
            anchor="w",
            padx=22,
            pady=(7, 0)
        )

        tk.Label(
            self.sidebar,
            text="Python\nTkinter\nGreedy Algorithm\nMatplotlib",
            font=("Arial", 8),
            bg=self.NAVY,
            fg="#9FB3C8",
            justify="left"
        ).pack(
            anchor="w",
            padx=22,
            pady=(12, 0)
        )

        # BOTTOM TEXT

        tk.Label(
            self.sidebar,
            text="SOLAR ENERGY",
            font=("Arial", 7, "bold"),
            bg=self.NAVY,
            fg="#5EEAD4"
        ).pack(
            side="bottom",
            pady=15
        )

    # =========================================================
    # SIDEBAR BUTTON
    # =========================================================

    def sidebar_item(
        self,
        text,
        command,
        active=False
    ):

        if active:
            bg = "#1D4ED8"
            fg = "white"
        else:
            bg = self.NAVY
            fg = "#D9E2EC"

        button = tk.Button(
            self.sidebar,
            text=text,
            command=command,
            font=(
                "Arial",
                9,
                "bold" if active else "normal"
            ),
            bg=bg,
            fg=fg,
            activebackground="#2563EB",
            activeforeground="white",
            bd=0,
            relief="flat",
            anchor="w",
            padx=20,
            cursor="hand2"
        )

        button.pack(
            fill="x",
            padx=12,
            pady=2,
            ipady=8
        )

    # =========================================================
    # MAIN AREA
    # =========================================================

    def create_main_area(self):

        self.main = tk.Frame(
            self.root,
            bg=self.BACKGROUND
        )

        self.main.pack(
            side="left",
            fill="both",
            expand=True
        )

    # =========================================================
    # HEADER
    # =========================================================

    def create_header(self):

        header = tk.Frame(
            self.main,
            bg=self.BACKGROUND,
            height=65
        )

        header.pack(
            fill="x",
            padx=22
        )

        header.pack_propagate(False)

        tk.Label(
            header,
            text="Solar Panel Placement Optimization",
            font=("Arial", 18, "bold"),
            bg=self.BACKGROUND,
            fg=self.TEXT
        ).pack(
            anchor="w",
            pady=(13, 0)
        )

        tk.Label(
            header,
            text="Intelligent energy location selection using Greedy Algorithm",
            font=("Arial", 8),
            bg=self.BACKGROUND,
            fg=self.MUTED
        ).pack(
            anchor="w"
        )

    # =========================================================
    # SOLAR BANNER
    # =========================================================

    def create_banner(self):

        banner_card = tk.Frame(
            self.main,
            bg=self.WHITE,
            highlightbackground=self.BORDER,
            highlightthickness=1
        )

        banner_card.pack(
            fill="x",
            padx=22,
            pady=(0, 10)
        )

        canvas = tk.Canvas(
            banner_card,
            height=105,
            bg="#EAF4FF",
            highlightthickness=0
        )

        canvas.pack(
            fill="x"
        )

        # Sky

        canvas.create_rectangle(
            0,
            0,
            1000,
            105,
            fill="#EAF4FF",
            outline=""
        )

        # Sun

        canvas.create_oval(
            45,
            18,
            90,
            63,
            fill="#FACC15",
            outline=""
        )

        # Sun rays

        for angle in range(
            0,
            360,
            45
        ):

            rad = math.radians(angle)

            x1 = 67 + math.cos(rad) * 30
            y1 = 40 + math.sin(rad) * 30

            x2 = 67 + math.cos(rad) * 39
            y2 = 40 + math.sin(rad) * 39

            canvas.create_line(
                x1,
                y1,
                x2,
                y2,
                fill="#F59E0B",
                width=2
            )

        # Text

        canvas.create_text(
            125,
            35,
            text="SMART SOLAR",
            font=("Arial", 17, "bold"),
            fill=self.NAVY,
            anchor="w"
        )

        canvas.create_text(
            125,
            60,
            text="ENERGY PLANNING",
            font=("Arial", 14, "bold"),
            fill=self.BLUE,
            anchor="w"
        )

        canvas.create_text(
            125,
            84,
            text="High-energy location selection using Greedy Strategy",
            font=("Arial", 8),
            fill=self.MUTED,
            anchor="w"
        )

        # Ground

        canvas.create_rectangle(
            540,
            82,
            1000,
            105,
            fill="#A7D7B5",
            outline=""
        )

        # Panels

        self.draw_solar_panel(
            canvas,
            565,
            60,
            125,
            55
        )

        self.draw_solar_panel(
            canvas,
            725,
            67,
            105,
            48
        )

    # =========================================================
    # DRAW SOLAR PANEL
    # =========================================================

    def draw_solar_panel(
        self,
        canvas,
        x,
        y,
        width,
        height
    ):

        canvas.create_polygon(
            x,
            y,
            x + width,
            y - 18,
            x + width + 20,
            y + height - 18,
            x + 20,
            y + height,
            fill="#173B63",
            outline=""
        )

        rows = 3
        cols = 5

        for r in range(rows):

            for c in range(cols):

                cell_w = width / cols
                cell_h = height / rows

                px = x + c * cell_w + 3
                py = y - 14 + r * cell_h

                canvas.create_rectangle(
                    px,
                    py,
                    px + cell_w - 5,
                    py + cell_h - 4,
                    fill="#2878A6",
                    outline="#6FB4D8"
                )

        # Stand

        canvas.create_line(
            x + 35,
            y + height,
            x + 55,
            y + 10,
            fill="#536D7E",
            width=3
        )

        canvas.create_line(
            x + width - 5,
            y + height - 12,
            x + width + 12,
            y + 5,
            fill="#536D7E",
            width=3
        )

    # =========================================================
    # WORKSPACE
    # =========================================================

    def create_workspace(self):

        workspace = tk.Frame(
            self.main,
            bg=self.BACKGROUND
        )

        workspace.pack(
            fill="both",
            expand=True,
            padx=22
        )

        # =========================
        # LEFT CARD
        # =========================

        left = tk.Frame(
            workspace,
            bg=self.WHITE,
            highlightbackground=self.BORDER,
            highlightthickness=1
        )

        left.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 5)
        )

        tk.Label(
            left,
            text="INPUT PARAMETERS",
            font=("Arial", 11, "bold"),
            bg=self.WHITE,
            fg=self.BLUE
        ).pack(
            anchor="w",
            padx=15,
            pady=(10, 5)
        )

        # Controls

        control = tk.Frame(
            left,
            bg=self.WHITE
        )

        control.pack(
            fill="x",
            padx=15
        )

        tk.Label(
            control,
            text="Number of Locations",
            font=("Arial", 8, "bold"),
            bg=self.WHITE,
            fg=self.MUTED
        ).grid(
            row=0,
            column=0,
            sticky="w"
        )

        self.location_entry = tk.Entry(
            control,
            width=9,
            font=("Arial", 10, "bold"),
            justify="center",
            bd=1,
            relief="solid"
        )

        self.location_entry.grid(
            row=1,
            column=0,
            padx=(0, 10),
            pady=(3, 6)
        )

        tk.Label(
            control,
            text="Panels to Install",
            font=("Arial", 8, "bold"),
            bg=self.WHITE,
            fg=self.MUTED
        ).grid(
            row=0,
            column=1,
            sticky="w"
        )

        self.panel_entry = tk.Entry(
            control,
            width=9,
            font=("Arial", 10, "bold"),
            justify="center",
            bd=1,
            relief="solid"
        )

        self.panel_entry.grid(
            row=1,
            column=1,
            padx=(0, 10),
            pady=(3, 6)
        )

        tk.Button(
            control,
            text="GENERATE",
            command=self.generate_inputs,
            font=("Arial", 8, "bold"),
            bg=self.BLUE,
            fg="white",
            activebackground="#1D4ED8",
            activeforeground="white",
            width=11,
            height=1,
            bd=0,
            cursor="hand2"
        ).grid(
            row=1,
            column=2,
            pady=(3, 6)
        )

        # Energy title

        tk.Label(
            left,
            text="ENERGY OUTPUT",
            font=("Arial", 9, "bold"),
            bg=self.WHITE,
            fg=self.GREEN
        ).pack(
            anchor="w",
            padx=15,
            pady=(0, 2)
        )

        tk.Label(
            left,
            text="Enter energy output manually for each location",
            font=("Arial", 7),
            bg=self.WHITE,
            fg=self.MUTED
        ).pack(
            anchor="w",
            padx=15
        )

        # Input grid

        self.input_grid = tk.Frame(
            left,
            bg=self.WHITE
        )

        self.input_grid.pack(
            fill="x",
            padx=12,
            pady=5
        )

        self.show_empty_message()

        # Bottom buttons

        button_frame = tk.Frame(
            left,
            bg=self.WHITE
        )

        button_frame.pack(
            side="bottom",
            fill="x",
            padx=12,
            pady=9
        )

        self.make_button(
            button_frame,
            "OPTIMIZE",
            self.optimize,
            self.GREEN
        )

        self.make_button(
            button_frame,
            "GRAPH",
            self.show_graph,
            self.PURPLE
        )

        self.make_button(
            button_frame,
            "CLEAR",
            self.clear,
            self.ORANGE
        )

        self.make_button(
            button_frame,
            "EXIT",
            self.root.destroy,
            self.RED
        )

        # =========================
        # RIGHT CARD
        # =========================

        right = tk.Frame(
            workspace,
            bg=self.WHITE,
            highlightbackground=self.BORDER,
            highlightthickness=1,
            width=330
        )

        right.pack(
            side="right",
            fill="both",
            expand=True,
            padx=(5, 0)
        )

        tk.Label(
            right,
            text="OPTIMIZATION SUMMARY",
            font=("Arial", 11, "bold"),
            bg=self.WHITE,
            fg=self.PURPLE
        ).pack(
            anchor="w",
            padx=15,
            pady=(10, 5)
        )

        # Metrics

        self.total_var = tk.StringVar(
            value="—"
        )

        self.selected_var = tk.StringVar(
            value="—"
        )

        self.average_var = tk.StringVar(
            value="—"
        )

        self.metric_card(
            right,
            "TOTAL ENERGY",
            self.total_var,
            self.GREEN
        )

        self.metric_card(
            right,
            "SELECTED LOCATIONS",
            self.selected_var,
            self.BLUE
        )

        self.metric_card(
            right,
            "AVERAGE ENERGY",
            self.average_var,
            self.PURPLE
        )

        # Result

        tk.Label(
            right,
            text="RESULT DETAILS",
            font=("Arial", 9, "bold"),
            bg=self.WHITE,
            fg=self.TEXT
        ).pack(
            anchor="w",
            padx=15,
            pady=(5, 3)
        )

        self.result = tk.Text(
            right,
            font=("Courier New", 8),
            bg="#F8FAFC",
            fg=self.TEXT,
            bd=0,
            height=8,
            padx=10,
            pady=8,
            wrap="word"
        )

        self.result.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(0, 10)
        )

        self.result.insert(
            "1.0",
            "Your optimization result will appear here.\n\n"
            "Enter project inputs and energy values,\n"
            "then click OPTIMIZE."
        )

    # =========================================================
    # BUTTON
    # =========================================================

    def make_button(
        self,
        parent,
        text,
        command,
        color
    ):

        tk.Button(
            parent,
            text=text,
            command=command,
            font=("Arial", 8, "bold"),
            bg=color,
            fg="white",
            activebackground=color,
            activeforeground="white",
            width=10,
            height=1,
            bd=0,
            cursor="hand2"
        ).pack(
            side="left",
            padx=(0, 5),
            ipady=3
        )

    # =========================================================
    # METRIC CARD
    # =========================================================

    def metric_card(
        self,
        parent,
        title,
        variable,
        color
    ):

        card = tk.Frame(
            parent,
            bg="#F8FAFC",
            highlightbackground=self.BORDER,
            highlightthickness=1
        )

        card.pack(
            fill="x",
            padx=15,
            pady=3
        )

        strip = tk.Frame(
            card,
            bg=color,
            width=4
        )

        strip.pack(
            side="left",
            fill="y"
        )

        inner = tk.Frame(
            card,
            bg="#F8FAFC"
        )

        inner.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=5
        )

        tk.Label(
            inner,
            text=title,
            font=("Arial", 7, "bold"),
            bg="#F8FAFC",
            fg=self.MUTED
        ).pack(
            anchor="w"
        )

        tk.Label(
            inner,
            textvariable=variable,
            font=("Arial", 11, "bold"),
            bg="#F8FAFC",
            fg=self.TEXT
        ).pack(
            anchor="w"
        )

    # =========================================================
    # EMPTY MESSAGE
    # =========================================================

    def show_empty_message(self):

        for widget in self.input_grid.winfo_children():
            widget.destroy()

        tk.Label(
            self.input_grid,
            text="Enter number of locations and click GENERATE",
            font=("Arial", 8),
            bg=self.WHITE,
            fg="#9CA3AF"
        ).pack(
            pady=15
        )

    # =========================================================
    # GENERATE INPUTS
    # =========================================================

    def generate_inputs(self):

        for widget in self.input_grid.winfo_children():
            widget.destroy()

        self.entries = []

        try:

            locations = int(
                self.location_entry.get()
            )

            panels = int(
                self.panel_entry.get()
            )

        except ValueError:

            messagebox.showerror(
                "Invalid Input",
                "Please enter valid numbers."
            )

            return

        if locations < 1 or locations > 8:

            messagebox.showerror(
                "Invalid Locations",
                "Please enter locations between 1 and 8."
            )

            return

        if panels < 1 or panels > locations:

            messagebox.showerror(
                "Invalid Panels",
                "Panels must be between 1 and locations."
            )

            return

        # Generate input boxes

        for i in range(locations):

            row = i // 4
            column = i % 4

            box = tk.Frame(
                self.input_grid,
                bg="#F8FAFC",
                highlightbackground=self.BORDER,
                highlightthickness=1
            )

            box.grid(
                row=row,
                column=column,
                padx=3,
                pady=3,
                sticky="nsew"
            )

            tk.Label(
                box,
                text=f"P{i + 1}",
                font=("Arial", 9, "bold"),
                bg="#F8FAFC",
                fg=self.BLUE
            ).pack(
                pady=(4, 1)
            )

            entry = tk.Entry(
                box,
                width=7,
                font=("Arial", 10, "bold"),
                justify="center",
                bd=1,
                relief="solid",
                bg="white"
            )

            entry.pack(
                padx=5,
                pady=2,
                ipady=3
            )

            tk.Label(
                box,
                text="Watts",
                font=("Arial", 6),
                bg="#F8FAFC",
                fg=self.MUTED
            ).pack(
                pady=(0, 4)
            )

            self.entries.append(
                entry
            )

        if self.entries:
            self.entries[0].focus_set()

    # =========================================================
    # OPTIMIZE
    # =========================================================

    def optimize(self):

        try:

            locations = int(
                self.location_entry.get()
            )

            panels = int(
                self.panel_entry.get()
            )

        except ValueError:

            messagebox.showerror(
                "Invalid Input",
                "Enter valid locations and panels."
            )

            return

        if len(self.entries) != locations:

            messagebox.showwarning(
                "Generate Inputs",
                "Please click GENERATE first."
            )

            return

        data = []

        # Read values

        for i, entry in enumerate(
            self.entries
        ):

            value_text = entry.get().strip()

            if value_text == "":

                messagebox.showerror(
                    "Missing Value",
                    f"Enter energy value for P{i + 1}."
                )

                entry.focus_set()

                return

            try:

                value = float(
                    value_text
                )

            except ValueError:

                messagebox.showerror(
                    "Invalid Value",
                    f"Enter a numeric value for P{i + 1}."
                )

                entry.focus_set()

                return

            if value < 0:

                messagebox.showerror(
                    "Invalid Energy",
                    f"Energy cannot be negative for P{i + 1}."
                )

                return

            data.append(
                (
                    f"P{i + 1}",
                    value
                )
            )

        # GREEDY ALGORITHM
        data.sort(
            key=lambda x: x[1],
            reverse=True
        )

        selected = data[:panels]

        # Calculations

        total = sum(
            value
            for name, value
            in selected
        )

        average = total / panels

        highest = max(
            value
            for name, value
            in data
        )

        lowest = min(
            value
            for name, value
            in data
        )

        overall_average = (
            sum(
                value
                for name, value
                in data
            )
            / locations
        )

        # Update cards

        self.total_var.set(
            f"{total:.2f} W"
        )

        self.selected_var.set(
            ", ".join(
                name
                for name, value
                in selected
            )
        )

        self.average_var.set(
            f"{average:.2f} W"
        )

        # Result

        self.result.delete(
            "1.0",
            tk.END
        )

        self.result.insert(
            tk.END,
            "GREEDY OPTIMIZATION RESULT\n"
        )

        self.result.insert(
            tk.END,
            "=" * 35 + "\n\n"
        )

        self.result.insert(
            tk.END,
            "SELECTED LOCATIONS\n"
        )

        self.result.insert(
            tk.END,
            "-" * 35 + "\n"
        )

        for name, value in selected:

            self.result.insert(
                tk.END,
                f"{name:<8} {value:>10.2f} W\n"
            )

        self.result.insert(
            tk.END,
            "\n"
        )

        self.result.insert(
            tk.END,
            f"Total Energy    : {total:.2f} W\n"
        )

        self.result.insert(
            tk.END,
            f"Average Energy  : {average:.2f} W\n"
        )

        self.result.insert(
            tk.END,
            f"Highest Output  : {highest:.2f} W\n"
        )

        self.result.insert(
            tk.END,
            f"Lowest Output   : {lowest:.2f} W\n"
        )

        self.result.insert(
            tk.END,
            f"Overall Average : {overall_average:.2f} W\n"
        )

        self.result.insert(
            tk.END,
            "\nALGORITHM\n"
        )

        self.result.insert(
            tk.END,
            "-" * 35 + "\n"
        )

        self.result.insert(
            tk.END,
            "Method : Greedy Algorithm\n"
        )

        self.result.insert(
            tk.END,
            "Strategy : Highest Energy First\n"
        )

        self.result.insert(
            tk.END,
            "Time : O(n log n)\n"
        )

        self.result.insert(
            tk.END,
            "Space : O(n)\n"
        )

    # =========================================================
    # GRAPH
    # =========================================================

    def show_graph(self):

        if not self.entries:

            messagebox.showwarning(
                "No Data",
                "Generate the input boxes first."
            )

            return

        names = []
        values = []

        for i, entry in enumerate(
            self.entries
        ):

            text = entry.get().strip()

            if text == "":

                messagebox.showerror(
                    "Missing Value",
                    f"Enter energy value for P{i + 1}."
                )

                return

            try:

                value = float(text)

            except ValueError:

                messagebox.showerror(
                    "Invalid Value",
                    f"Invalid value for P{i + 1}."
                )

                return

            if value < 0:

                messagebox.showerror(
                    "Invalid Energy",
                    f"Energy cannot be negative for P{i + 1}."
                )

                return

            names.append(
                f"P{i + 1}"
            )

            values.append(
                value
            )

        # Graph

        plt.figure(
            figsize=(9, 5)
        )

        bars = plt.bar(
            names,
            values
        )

        plt.title(
            "Solar Panel Energy Output Analysis",
            fontsize=15,
            fontweight="bold"
        )

        plt.xlabel(
            "Panel Location"
        )

        plt.ylabel(
            "Energy Output (Watts)"
        )

        plt.grid(
            axis="y",
            linestyle="--",
            alpha=0.3
        )

        max_value = max(values)

        for bar, value in zip(
            bars,
            values
        ):

            plt.text(
                bar.get_x()
                + bar.get_width() / 2,
                value + max_value * 0.02,
                f"{value:.0f}",
                ha="center",
                fontsize=9
            )

        plt.tight_layout()

        plt.show()

    # =========================================================
    # CLEAR
    # =========================================================

    def clear(self):

        self.location_entry.delete(
            0,
            tk.END
        )

        self.panel_entry.delete(
            0,
            tk.END
        )

        self.entries = []

        self.show_empty_message()

        self.total_var.set(
            "—"
        )

        self.selected_var.set(
            "—"
        )

        self.average_var.set(
            "—"
        )

        self.result.delete(
            "1.0",
            tk.END
        )

        self.result.insert(
            "1.0",
            "Your optimization result will appear here.\n\n"
            "Enter project inputs and energy values,\n"
            "then click OPTIMIZE."
        )

    # =========================================================
    # DASHBOARD
    # =========================================================

    def show_dashboard(self):

        self.result.delete(
            "1.0",
            tk.END
        )

        self.result.insert(
            "1.0",
            "DASHBOARD\n"
            "===================================\n\n"
            "SOLAR PANEL PLACEMENT OPTIMIZATION\n\n"
            "This application selects high-energy\n"
            "solar panel locations using the\n"
            "Greedy Algorithm.\n\n"
            "WORKFLOW\n"
            "1. Enter number of locations\n"
            "2. Enter panels to install\n"
            "3. Click GENERATE\n"
            "4. Enter energy values\n"
            "5. Click OPTIMIZE\n"
            "6. View result and graph"
        )

    # =========================================================
    # GREEDY ALGORITHM
    # =========================================================

    def show_greedy(self):

        self.result.delete(
            "1.0",
            tk.END
        )

        self.result.insert(
            "1.0",
            "GREEDY ALGORITHM\n"
            "===================================\n\n"
            "STRATEGY\n"
            "Highest Energy First\n\n"
            "STEPS\n"
            "1. Read energy values\n"
            "2. Sort locations in descending order\n"
            "3. Select highest-energy locations\n"
            "4. Calculate total energy\n"
            "5. Display selected locations\n\n"
            "TIME COMPLEXITY\n"
            "O(n log n)\n\n"
            "SPACE COMPLEXITY\n"
            "O(n)"
        )

    # =========================================================
    # ENERGY ANALYSIS
    # =========================================================

    def show_energy(self):

        if not self.entries:

            messagebox.showinfo(
                "Energy Analysis",
                "Generate the inputs and enter energy values first."
            )

            return

        self.show_graph()

    # =========================================================
    # OPTIMIZATION
    # =========================================================

    def show_optimization(self):

        if not self.entries:

            messagebox.showinfo(
                "Optimization",
                "Generate the inputs first."
            )

            return

        self.optimize()


# =============================================================
# MAIN
# =============================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = SolarPanelApp(
        root
    )

    root.mainloop()