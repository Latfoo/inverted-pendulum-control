# Inverted Pendulum

This project is a first look into controlling an inverted Pendulum using the Gymnasium Environemt by Farama-Foundation.
The pendulum starts in randomized state and is then controlled by a PD-Controller. Meanwhile random torque disturbances are being forced upon the pendulum.
If terminated or truncated, the whole environment is being resetted. Each episode is being recorded and added to the results folder automatically.

# Example Terminal Output

```bash
Running PD control with disturbances — press Ctrl+C to stop.
Disturbance torque: 2.16
Environment reset...
Saved episode 0
Disturbance torque: 2.78
Environment reset...
Saved episode 1
Disturbance torque: 2.65

Stopped by user.
```

---

## Technologies Used

- Python 3.10
- [Gymnasium (`Pendulum-v1`)](https://github.com/Farama-Foundation/Gymnasium)
- NumPy
- Pygame

---

## Setup (Conda recommended)

```bash
conda env create -f environment.yml
```

---

## Project Structure

```
inverted-pendulum-control/
├── pendulum_pd.py
├── results/
├── environment.yml
└── README.md
```

---

## Author

Latfoo
