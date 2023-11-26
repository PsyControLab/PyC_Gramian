import numpy as np
import control as ct
from slycot import sb03md

def PyC_gram(sys):
    """
    Compute the Controllability Gramian for a given state-space system.

    Parameters:
    sys (StateSpace): The state-space representation of the system.

    Returns:
    numpy.ndarray: The Controllability Gramian of the system.
    """
    dico = 'D'  # 'D' for discrete-time
    if np.any(np.linalg.eigvals(sys.A).real >= 1.0):
        raise ValueError("Oops, the system is unstable!")
    n = sys.nstates
    U = np.zeros((n, n))
    A = np.array(sys.A)
    g = -sys.B @ sys.B.T
    X, scale, sep, ferr, w = sb03md(n, g, A, U, dico, job='X', fact='N', trana='T')
    gram = X
    return gram

def PyC_compute_gramians(df):
    """
    Compute the Controllability Gramians for each row in a DataFrame.

    Parameters:
    df (pandas.DataFrame): DataFrame containing the system matrices.

    Returns:
    pandas.DataFrame: The original DataFrame with an additional column for Gramians.
    """
    gramian_list_N = []

    for index, row in df.iterrows():
        A = np.array(row['A_Norm'])
        B = np.array(row['B_matrice'].reshape(28,1))
        m = A.shape[0]
        C = np.zeros((1,m))
        D = 0
        sys = ct.ss(A, B, C, D, dt=None)
        gramian_N = PyC_gram(sys)
        gramian_list_N.append(gramian_N)

    df['gram'] = gramian_list_N
    df['eig_gram'] = df['gram'].apply(lambda x: np.real(np.linalg.eigvals(x)))
    df['eig_gram_abs'] = df['eig_gram'].apply(lambda x: np.abs(x))
    df['eig_gram_abs_min'] = df['eig_gram_abs'].apply(lambda x: np.min(x))
    df['eig_gram_abs_mean'] = df['eig_gram_abs'].apply(lambda x: np.mean(x))
    df['eig_gram_abs_median'] = df['eig_gram_abs'].apply(lambda x: np.median(x))
    return df

# Example usage:
# df = ... # Your DataFrame with 'A_Norm' and 'B_matrice' columns
# df_with_grams = PyC_compute_gramians(df)
# print(df_with_grams.head(2))
