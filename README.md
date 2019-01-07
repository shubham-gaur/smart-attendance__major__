# Intelligent Attendance Management System
A system designed to automate the process of attendance management. It comprises of various modules consisting detection and recognition of faces take from web cam/ IP cameras.
<p> Complete UI has been designed with PyQT. A tool to write UI with raw python code. 

### Algorithm
Eigenfaces is the name given to a set of eigenvectors when they are used in the computer vision problem of human face recognition. The approach of using eigenfaces for recognition was developed by Sirovich and Kirby (1987) and used by Matthew Turk and Alex Pentland in face classification.The eigenvectors are derived from the covariance matrix of the probability distribution over the high-dimensional vector space of face images. The eigenfaces themselves form a basis set of all images used to construct the covariance matrix. This produces dimension reduction by allowing the smaller set of basis images to represent the original training images. Classification can be achieved by comparing how faces are represented by the basis set.

#### Algorithmic Description
Let  be a random vector with observations  .
1. Compute the mean  
1. Compute the the Covariance Matrix S
1. Compute the eigenvalues  and eigenvectors.`
1. Order the eigenvectors descending by their eigenvalue. The  principal components are the eigenvectors corresponding to the  largest eigenvalues.
1. The  principal components of the observed vector.
1. Reconstruction from the PCA.

The Eigen faces method then performs face recognition by:
* Projecting all training samples into the PCA subspace.
* Projecting the query image into the PCA subspace.
* Finding the nearest neighbour between the projected training images and the projected query image.

Still there’s one problem left to solve. Imagine we are given 400  images sized 100 X 100 pixel. The Principal Component Analysis solves the covariance matrix **S = XX^T**  , where **SIZE(X) = 1000 X 400** in our example. You would end up with a **10000 X 10000**  matrix, roughly ***0.8 GB***  . Solving this problem isn’t feasible, so we’ll need to apply a trick. From your linear algebra lessons you know that a  matrix with  can only have  non-zero eigenvalues. So it’s possible to take the eigenvalue decomposition  of size  instead:
 
and get the original eigenvectors of  with a left multiplication of the data matrix:
 
The resulting eigenvectors are orthogonal, to get orthonormal eigenvectors they need to be normalized to unit length. I don’t want to turn this into a publication, so please look into [Duda01] for the derivation and proof of the equations.

### main.py
### db_connect.py

## Conclusion
