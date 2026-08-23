import matplotlib.pyplot as plt
import numpy as np

# ============================================================
# Interaktive geometrische Figur
#
# Die beiden oberen Punkte können frei horizontal und
# vertikal mit der Maus verschoben werden.
#
# Die blaue Strecke zeigt die Höhe des Schnittpunktes der
# beiden roten Diagonalen über der Grundlinie.
#
# Eine wichtige Eigenschaft der Figur wird dabei sichtbar:
# Die Länge der blauen Strecke hängt NICHT vom horizontalen
# Abstand der beiden senkrechten Linien ab.
# ============================================================


# ------------------------------------------------------------
# Einstellungen
# ------------------------------------------------------------

# Größe des Anzeigebereichs
VIEW_WIDTH = 25.0
VIEW_HEIGHT = 25.0

# Anfangspositionen der beiden oberen Punkte
left_x = 7.5
left_height = 15.0

right_x = 17.5
right_height = 10.0

# Mindesthöhe der Punkte
MIN_HEIGHT = 0.5

# Minimaler horizontaler Abstand der senkrechten Linien
MIN_DISTANCE = 1.0

step = 0.1

# ------------------------------------------------------------
# Berechnung des Schnittpunktes
# ------------------------------------------------------------

def intersection(x1, h1, x2, h2):
    """
    Berechnet den Schnittpunkt der beiden roten Diagonalen.

    Linke Diagonale:
        (x1, h1) -> (x2, 0)

    Rechte Diagonale:
        (x1, 0) -> (x2, h2)

    Rückgabe:
        x, y des Schnittpunktes
    """

    # Horizontale Breite der Figur
    width = x2 - x1

    # Höhe des Schnittpunktes
    y = h1 * h2 / (h1 + h2)

    # Horizontale Position des Schnittpunktes
    x = x1 + width * h1 / (h1 + h2)

    return x, y


# ------------------------------------------------------------
# Abbildung vorbereiten
# ------------------------------------------------------------

fig, ax = plt.subplots(figsize=(8, 8))

fig.canvas.manager.set_window_title(
    "Höhe zwischen zwei Masten"
)

# Gleiche Skalierung für x und y
ax.set_aspect("equal", adjustable="box")

# Fester Anzeigebereich
ax.set_xlim(0, VIEW_WIDTH)
ax.set_ylim(0, VIEW_HEIGHT)

#ax.axis("off")
ax.axis("on")
ax.grid(True)

# ------------------------------------------------------------
# Anfangsposition des Schnittpunktes
# ------------------------------------------------------------

intersection_x, intersection_y = intersection(
    left_x,
    left_height,
    right_x,
    right_height
)


# ------------------------------------------------------------
# Grundlinie
# ------------------------------------------------------------

base_line, = ax.plot(
    [0, VIEW_WIDTH],
    [0, 0],
    color="black",
    linewidth=2.5
)


# ------------------------------------------------------------
# Senkrechte schwarze Linien
# ------------------------------------------------------------

left_vertical, = ax.plot(
    [left_x, left_x],
    [0, left_height],
    color="black",
    linewidth=2.5
)

right_vertical, = ax.plot(
    [right_x, right_x],
    [0, right_height],
    color="black",
    linewidth=2.5
)


# ------------------------------------------------------------
# Rote Diagonalen
# ------------------------------------------------------------

red_left, = ax.plot(
    [left_x, right_x],
    [left_height, 0],
    color="red",
    linewidth=2.5
)

red_right, = ax.plot(
    [left_x, right_x],
    [0, right_height],
    color="red",
    linewidth=2.5
)


# ------------------------------------------------------------
# Blaue Linie
# ------------------------------------------------------------

blue_line, = ax.plot(
    [intersection_x, intersection_x],
    [0, intersection_y],
    color="steelblue",
    linewidth=3
)


# ------------------------------------------------------------
# Schnittpunkt markieren
# ------------------------------------------------------------

intersection_point, = ax.plot(
    [intersection_x],
    [intersection_y],
    marker="o",
    color="steelblue",
    markersize=7
)


# ------------------------------------------------------------
# Verschiebbare obere Punkte
# ------------------------------------------------------------

left_handle, = ax.plot(
    [left_x],
    [left_height],
    marker="o",
    color="black",
    markersize=11,
    markerfacecolor="white",
    markeredgewidth=2
)

right_handle, = ax.plot(
    [right_x],
    [right_height],
    marker="o",
    color="black",
    markersize=11,
    markerfacecolor="white",
    markeredgewidth=2
)


# ------------------------------------------------------------
# Beschriftungen der senkrechten Linien
# ------------------------------------------------------------

left_label = ax.text(
    left_x - 0.4,
    left_height / 2,
    f"{left_height:.2f}",
    ha="right",
    va="center",
    fontsize=15,
    fontweight="bold"
)

right_label = ax.text(
    right_x + 0.4,
    right_height / 2,
    f"{right_height:.2f}",
    ha="left",
    va="center",
    fontsize=15,
    fontweight="bold"
)


# ------------------------------------------------------------
# Beschriftung der blauen Linie
# ------------------------------------------------------------

blue_label = ax.text(
    intersection_x + 0.35,
    intersection_y / 2,
    f"{intersection_y:.2f}",
    ha="left",
    va="center",
    fontsize=15,
    color="steelblue",
    fontweight="bold"
)


# ------------------------------------------------------------
# Überschrift
# ------------------------------------------------------------

ax.text(
    VIEW_WIDTH / 2,
    VIEW_HEIGHT - 0.8,
    "Höhe am Schnittpunkt der Diagonalen",
    ha="center",
    va="center",
    fontsize=12
)


# ------------------------------------------------------------
# Aktuell bewegter Punkt
# ------------------------------------------------------------

dragging = None


# ------------------------------------------------------------
# Zeichnung aktualisieren
# ------------------------------------------------------------

def update_figure():

    global left_x
    global right_x
    global left_height
    global right_height

    # Schnittpunkt neu berechnen
    x, y = intersection(
        left_x,
        left_height,
        right_x,
        right_height
    )

    # --------------------------------------------------------
    # Schwarze senkrechte Linien
    # --------------------------------------------------------

    left_vertical.set_data(
        [left_x, left_x],
        [0, left_height]
    )

    right_vertical.set_data(
        [right_x, right_x],
        [0, right_height]
    )

    # --------------------------------------------------------
    # Rote Diagonalen
    # --------------------------------------------------------

    red_left.set_data(
        [left_x, right_x],
        [left_height, 0]
    )

    red_right.set_data(
        [left_x, right_x],
        [0, right_height]
    )

    # --------------------------------------------------------
    # Blaue Linie
    #
    # Sie folgt dem tatsächlichen Schnittpunkt.
    # --------------------------------------------------------

    blue_line.set_data(
        [x, x],
        [0, y]
    )

    # --------------------------------------------------------
    # Schnittpunkt
    # --------------------------------------------------------

    intersection_point.set_data(
        [x],
        [y]
    )

    # --------------------------------------------------------
    # Obere Punkte
    # --------------------------------------------------------

    left_handle.set_data(
        [left_x],
        [left_height]
    )

    right_handle.set_data(
        [right_x],
        [right_height]
    )

    # --------------------------------------------------------
    # Beschriftungen
    # --------------------------------------------------------

    left_label.set_position(
        (left_x - 0.4, left_height / 2)
    )

    left_label.set_text(
        f"{left_height:.2f}"
    )

    right_label.set_position(
        (right_x + 0.4, right_height / 2)
    )

    right_label.set_text(
        f"{right_height:.2f}"
    )

    blue_label.set_position(
        (x + 0.35, y / 2)
    )

    blue_label.set_text(
        f"{y:.2f}"
    )

    # Fester Anzeigebereich
    ax.set_xlim(0, VIEW_WIDTH)
    ax.set_ylim(0, VIEW_HEIGHT)

    fig.canvas.draw_idle()


# ------------------------------------------------------------
# Mausklick
# ------------------------------------------------------------

def mouse_press(event):

    global dragging

    if (
        event.inaxes != ax
        or event.xdata is None
        or event.ydata is None
    ):
        return

    # Abstand zum linken Punkt
    distance_left = (
        (event.xdata - left_x) ** 2
        + (event.ydata - left_height) ** 2
    ) ** 0.5

    # Abstand zum rechten Punkt
    distance_right = (
        (event.xdata - right_x) ** 2
        + (event.ydata - right_height) ** 2
    ) ** 0.5

    # Punkt auswählen
    if distance_left < 1.0:
        dragging = "left"

    elif distance_right < 1.0:
        dragging = "right"


# ------------------------------------------------------------
# Mausbewegung
# ------------------------------------------------------------

def mouse_move(event):

    global left_x
    global right_x
    global left_height
    global right_height

    if (
        dragging is None
        or event.inaxes != ax
        or event.xdata is None
        or event.ydata is None
    ):
        return

    # --------------------------------------------------------
    # Neue Koordinaten
    # --------------------------------------------------------

    new_x = max(
        0.0,
        min(VIEW_WIDTH, event.xdata)
    )

    new_y = max(
        MIN_HEIGHT,
        min(VIEW_HEIGHT, event.ydata)
    )

    new_x = np.round(new_x / step)*step
    new_y = np.round(new_y / step)*step

    # --------------------------------------------------------
    # Linken Punkt bewegen
    # --------------------------------------------------------

    if dragging == "left":

        # Mindestabstand zum rechten Punkt
        new_x = min(
            new_x,
            right_x - MIN_DISTANCE
        )

        # Falls der rechte Punkt sehr weit links liegt
        new_x = max(0.0, new_x)

        left_x = new_x
        left_height = new_y

    # --------------------------------------------------------
    # Rechten Punkt bewegen
    # --------------------------------------------------------

    elif dragging == "right":

        # Mindestabstand zum linken Punkt
        new_x = max(
            new_x,
            left_x + MIN_DISTANCE
        )

        new_x = min(
            VIEW_WIDTH,
            new_x
        )

        right_x = new_x
        right_height = new_y

    # Zeichnung aktualisieren
    update_figure()


# ------------------------------------------------------------
# Maustaste loslassen
# ------------------------------------------------------------

def mouse_release(event):

    global dragging

    dragging = None


# ------------------------------------------------------------
# Maus-Ereignisse registrieren
# ------------------------------------------------------------

fig.canvas.mpl_connect(
    "button_press_event",
    mouse_press
)

fig.canvas.mpl_connect(
    "motion_notify_event",
    mouse_move
)

fig.canvas.mpl_connect(
    "button_release_event",
    mouse_release
)


# ------------------------------------------------------------
# Programm starten
# ------------------------------------------------------------

plt.show()
