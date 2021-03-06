import numpy as np
from scipy.linalg import expm
import Rotation_Matrices


def euler_method_rotation_matrix():
    print("Inertia")
    inertia_list = list(map(float, input().split()))  # takes input as numbers with appropriate spaces
    inertia_tensor = np.array(inertia_list).reshape(3, 3)  # converts the list of numbers into the inertia tensor

    print("Torque")
    torque_list = list(map(float, input().split()))  # takes input as numbers with appropriate spaces
    torque_vector = np.array(torque_list)  # converts the list of numbers into the momentum vector

    print("Angular Velocity")
    omega_list = list(map(float, input().split()))  # takes input as numbers with appropriate spaces
    omega_initial = np.array(omega_list)  # converts the list of numbers into the initial angular velocity

    print("Euler Angles")
    theta = list(map(float, input().split()))  # takes three euler angles in degrees (XYZ)
    rotation_matrix = [Rotation_Matrices.euler_to_rotation_matrix(theta)]  # list to rotation matrix which is stored

    print("Initial Time")
    t_initial = float(input())  # initial time
    print("Final Time")
    t_final = float(input())  # final time
    print("Number of iterations")
    number_of_iterations = int(input())

    del_t = (t_final - t_initial) / number_of_iterations  # delta t for rotation matrix and Euler's equation

    omega = [omega_initial]  # all the values of omega will be stored here
    inertia_inv = np.linalg.inv(inertia_tensor)  # pre calculated value of the inverse of the inertia tensor

    for k in range(0, number_of_iterations):
        omega_hat = np.array([[0, -omega[k][2], omega[k][1]],  # to find the cross product matrix
                              [omega[k][2], 0, -omega[k][0]],
                              [-omega[k][1], omega[k][0], 0]])

        angular_momentum = np.array(np.dot(np.dot(inertia_tensor, omega_hat), omega[k]))  # the term (IOmega)xOmega

        next_omega = omega[k] + del_t * (np.dot(inertia_inv, (angular_momentum + torque_vector)))  # Euler's Method

        omega.append(next_omega)

        next_rotation_matrix = np.dot(rotation_matrix[k], expm(omega_hat * del_t))  # updating the Rotation Matrix

        rotation_matrix.append(next_rotation_matrix)

    # print(omega, rotation_matrix)

    return rotation_matrix


def euler_method_omega_vector():
    print("Inertia")
    inertia_list = list(map(float, input().split()))  # takes input as numbers with appropriate spaces
    inertia_tensor = np.array(inertia_list).reshape(3, 3)  # converts the list of numbers into the inertia tensor

    print("Torque")
    torque_list = list(map(float, input().split()))  # takes input as numbers with appropriate spaces
    torque_vector = np.array(torque_list)  # converts the list of numbers into the momentum vector

    print("Angular Velocity")
    omega_list = list(map(float, input().split()))  # takes input as numbers with appropriate spaces
    omega_initial = np.array(omega_list)  # converts the list of numbers into the initial angular velocity

    print("Euler Angles")
    theta = list(map(float, input().split()))  # takes three euler angles in degrees (XYZ)
    rotation_matrix = [Rotation_Matrices.euler_to_rotation_matrix(theta)]  # list to rotation matrix which is stored

    print("Initial Time")
    t_initial = float(input())  # initial time
    print("Final Time")
    t_final = float(input())  # final time
    print("Number of iterations")
    number_of_iterations = int(input())

    del_t = (t_final - t_initial) / number_of_iterations  # delta t for rotation matrix and Euler's equation

    omega = [omega_initial]  # all the values of omega will be stored here
    inertia_inv = np.linalg.inv(inertia_tensor)  # pre calculated value of the inverse of the inertia tensor

    for k in range(0, number_of_iterations):
        omega_hat = np.array([[0, -omega[k][2], omega[k][1]],  # to find the cross product matrix
                              [omega[k][2], 0, -omega[k][0]],
                              [-omega[k][1], omega[k][0], 0]])

        angular_momentum = np.array(np.dot(np.dot(inertia_tensor, omega_hat), omega[k]))  # the term (IOmega)xOmega

        next_omega = omega[k] + del_t * (np.dot(inertia_inv, (angular_momentum + torque_vector)))  # Euler's Method

        omega.append(next_omega)

        next_rotation_matrix = np.dot(rotation_matrix[k], expm(omega_hat * del_t))  # updating the Rotation Matrix

        rotation_matrix.append(next_rotation_matrix)

    # print(omega, rotation_matrix)

    return omega

