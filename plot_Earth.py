from mayavi import mlab
from tvtk.api import tvtk # python wrappers for the C++ vtk ecosystem
import constants

def plot_Earth(image_file):
    # create a figure window (and scene)
    fig = mlab.figure(size=(600, 600))
    
    # load and map the texture
    img = tvtk.JPEGReader()
    img.file_name = image_file
    texture = tvtk.Texture(input_connection=img.output_port, interpolate=1)
    # (interpolate for a less raster appearance when zoomed in)

    # use a TexturedSphereSource, a.k.a. getting our hands dirty
    
    Nrad = 180

    # create the sphere source with a given radius and angular resolution
    sphere = tvtk.TexturedSphereSource(radius=constants.R_e, theta_resolution=Nrad,
                                       phi_resolution=Nrad)

    # assemble rest of the pipeline, assign texture    
    sphere_mapper = tvtk.PolyDataMapper(input_connection=sphere.output_port)
    sphere_actor = tvtk.Actor(mapper=sphere_mapper, texture=texture)
    fig.scene.add_actor(sphere_actor)

    #mlab.plot3d(X_sat, Y_sat, Z_sat, color = (1,1,1), representation = "wireframe")
    #mlab.quiver3d(np.array([0,0,0]),np.array([0,0,0]),np.array([0,0,0]),np.array([R*2,0,0]),np.array([0,R*2,0]),np.array([0,0,R*2]), line_width = '1', color = (1,1,1))

    

# if __name__ == "__main__":
#     image_file = "world.topo.bathy.200412.3x5400x2700.jpeg"
#     plot_Earth(image_file)
    