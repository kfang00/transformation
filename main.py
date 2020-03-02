from display import *
from draw import *
from parse import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

parse_file( 'script', edges, transform, screen, color )

print_matrix(make_translate( 2,3,4 ))
print_matrix(make_scale( 2,3,4 ))
print_matrix(make_rotX(30))
print_matrix(make_rotY(30))
print_matrix(make_rotZ(30))
