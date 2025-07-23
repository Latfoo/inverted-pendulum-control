# Inverted Pendulum

This project is a first look into controlling an inverted Pendulum using the Gymnasium Environemt by Farama-Foundation.
The pendulum starts in randomized state and is then controlled by a PD-Controller. Meanwhile random torque disturbances are being forced upon the pendulum. If terminated or truncated, the whole environment is being resetted.

### Note on Video Recording

Earlier versions of this project included a video recording feature using `moviepy` and `ffmpeg`.  
To improve cross-platform compatibility and simplify setup, this feature has been removed.

As a result:
- The animation now runs live via `render_mode="human"`.
- Users on Windows, macOS, and Linux can view it directly with no extra dependencies.
- Some comments and code snippets related to video export remain in the source for reference.

## Demo

![Demo](results/gif/pd_control-episode-0.gif)

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

## Technologies Used

- Python 3.10
- [Gymnasium (`Pendulum-v1`)](https://github.com/Farama-Foundation/Gymnasium)
- NumPy
- Pygame

## Setup and Run
Make sure you have [Conda](https://docs.conda.io) (or Anaconda) installed.

Go into the project directory and type following command to create the environment.
```bash
conda env create -f environment.yml
```
To activate (if you have a different environment name, swap it for rl-env):
```bash
conda activate rl-env
```
To run:
```bash
python pendulum_pd.py
```
## Author

Latfoo
