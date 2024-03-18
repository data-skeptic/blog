# Modeling Group Behavior

Our guest in this episode is Sebastien Motsch, an assistant professor at Arizona State University, working in the School of Mathematical and Statistical Science. He works on modeling self-organized biological systems to understand how complex patterns emerge. 

Sebastien discussed two approaches to modeling the group behavior of animals, for instance, a flock of birds. He discussed how Boltzmann's questions and kinetic theory help them understand birds' interactions with respect to velocity changes. Sebastian also discussed the computational challenge of dealing with non-linear models.

Sebastien shared how the particular behavior of a group leads to a pattern. He also discussed how the flock determines the direction to go using the Vicsek model and Swarmalator. He shared how they collect data to study ants as well. 

Sebastien talked about the dynamics of consensus, particularly explaining heterophilous. He shared some assumptions made during modeling and why they were necessary. He also discussed the emerging behaviors in slime molds.

Rounding up, he gave some advice for students who wish to get into the field.  

## Papers discussed

[A new model for self-organized dynamics and its flocking behavior](https://arxiv.org/abs/1102.5575)

[Heterophilious dynamics enhances consensus](https://arxiv.org/abs/1301.4123)

## Resource



* Boltzmann equation

$$

f(t + \Delta t, \mathbf{x} + \Delta \mathbf{x}, \mathbf{v} + \Delta \mathbf{v}) = f(t, \mathbf{x}, \mathbf{v}) + \left( \frac{\partial f}{\partial t} \right)_{\text{coll}}

$$


Δt, Δx, and Δv represent small changes in time, position, and velocity.

(∂t/∂f)coll is the change in f due to collisions.


* Navier-Stokes equation

$$

\frac{\partial \mathbf{u}}{\partial t} + (\mathbf{u} \cdot \nabla) \mathbf{u} = -\frac{1}{\rho} \nabla p + \nu \nabla^2 \mathbf{u} + \mathbf{f}

$$

Where:

- "u" represents the velocity field of the fluid.

- "t" is time, representing the temporal dimension over which the fluid's behavior is analyzed.

- "rho (ρ)" is the fluid density.

- "p" is the pressure field within the fluid.

- "nabla p (▽p)" represents the gradient of the pressure field.

- ""nabla squared u (▽²u)" is the Laplacian of the velocity field.

- "f" represents external forces acting on the fluid.
