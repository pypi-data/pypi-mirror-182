import torch
import pypose as pp
from torch import nn


class NTI(pp.module.System):
    '''
    A rotation system expressed by LieTensor.
    '''
    def __init__(self):
        super().__init__()

    def state_transition(self, state, input, t=None):
        return input.Exp() @ state

    def observation(self, state, input, t=None):
        return state

model = NTI()
ekf = pp.module.EKF(model)

T = 5 # steps, state dim
states = pp.identity_SO3(T) # Rotation
inputs = pp.randn_so3(T, sigma=0.1) # Rotation velcocity
observ = pp.identity_SO3(T)
estim = pp.randn_SO3(T, sigma=100)
q, r = 0.01, 0.01
Q = torch.eye(4) * q
R = torch.eye(4) * r
cov = torch.zeros(T, 4, 4)

for i in range(T - 1):

    w = pp.randn_SO3(sigma=q) # transition noise
    v = pp.randn_SO3(sigma=r) # observation noise
    states[i+1], observ[i] = model(w @ states[i], inputs[i])
    estim[i+1], cov[i+1] = ekf(estim[i], v @ observ[i], inputs[i], cov[i], Q, R)

print('Est error:', (states-estim).norm(dim=-1))



# class NTI(pp.module.System):
#     '''
#     A nonlinear time invariant (NTI) system.
#     '''
#     def __init__(self):
#         super().__init__()

#     def state_transition(self, state, input, t=None):
#         return state.cos() + input

#     def observation(self, state, input, t):
#         return state.sin() + input

# model = NTI()
# ekf = pp.module.EKF(model)

# T, N = 5, 2 # steps, state dim
# # std of transition, observation, and estimation
# q, r, p = 0.1, 0.1, 10
# states = torch.zeros(T, N)
# inputs = torch.randn(T, N)
# observ = torch.zeros(T, N)
# estim = torch.randn(T, N) * p
# Q = torch.eye(N) * q**2
# R = torch.eye(N) * r**2
# P = torch.eye(N).repeat(T, 1, 1) * p**2

# for i in range(T - 1):

#     w = q * torch.randn(N) # transition noise
#     v = r * torch.randn(N) # observation noise
#     states[i+1], observ[i] = model(states[i] + w, inputs[i])
#     estim[i+1], P[i+1] = ekf(estim[i], observ[i] + v, inputs[i], P[i], Q, R)

# print('Est error:', (states-estim).norm(dim=-1))



# x = pp.randn_rxso3(5, requires_grad=True, device='cuda')
# el = x.euler()
# print(el)
# el.sum().backward()
# print(x.grad)

# y = pp.euler2SO3(el)
# print(x.rotation(), y)

# class NTI(pp.module.System):
#     '''
#     A nonlinear time invariant (NTI) system.
#     '''
#     def __init__(self):
#         super().__init__()

#     def state_transition(self, state, input, t=None):
#         return state.cos() + input

#     def observation(self, state, input, t):
#         return state.sin() + input

# model = NTI()
# ekf = pp.module.EKF(model)

# T, N = 5, 2 # steps, state dim
# # std of transition, observation, and estimation
# q, r, p = 0.1, 0.1, 10
# states = torch.zeros(T, N)
# inputs = torch.randn(T, N)
# observ = torch.zeros(T, N)
# estim = torch.randn(T, N) * p
# Q = torch.eye(N) * q**2
# R = torch.eye(N) * r**2
# P = torch.eye(N).repeat(T, 1, 1) * p**2

# for i in range(T - 1):

#     w = q * torch.randn(N) # transition noise
#     v = r * torch.randn(N) # observation noise
#     states[i+1], observ[i] = model(states[i] + w, inputs[i])
#     estim[i+1], P[i+1] = ekf(estim[i], observ[i] + v, inputs[i], P[i], Q, R)

# print('Est error:', (states-estim).norm(dim=-1))

# input = pp.randn_SE3(2)
# input.cumprod(dim = 0)
# x1 = input.cumops(dim = 0,  ops = lambda a, b : a @ b)
# x2 = pp.cumops(input, 0, lambda a, b : a @ b)
# print(x1, x2)

class PoseInv(nn.Module):
    def __init__(self, *dim):
        super().__init__()
        self.pose = pp.Parameter(pp.randn_SE3(*dim))

    def forward(self, inputs):
        return (self.pose @ inputs).Log().tensor()

B1, B2, M, N = 2, 3, 2, 2
device = torch.device("cuda" if not torch.cuda.is_available() else "cpu")
inputs = pp.randn_SE3(B1, B2, M, N).to(device)
invnet = PoseInv(M, N).to(device)
strategy = pp.optim.strategy.TrustRegion(radius=1e6)
optimizer = pp.optim.LM(invnet, strategy=strategy)

for idx in range(10):
    loss = optimizer.step(inputs)
    print('Pose loss %.7f @ %dit'%(loss, idx))
    if loss < 1e-5:
        print('Early Stoping!')
        print('Optimization Early Done with loss:', loss.item())
        break

assert idx < 9, "Optimization requires too many steps."