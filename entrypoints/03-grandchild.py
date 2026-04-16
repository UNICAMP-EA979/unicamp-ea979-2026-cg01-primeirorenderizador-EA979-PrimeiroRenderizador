import numpy as np
import urenderer

# Crie uma cena com três objetos, um filho do outro:
# Objeto0 -> Objeto1 -> Objeto2
#
# Configure as transformações para que todos os objetos sejam visíveis e renderize a cena
#
# Altere a transformação do objeto avô dos outros e renderize a cena.
# Observe como que os objetos filhos se movem juntos

if __name__ == "__main__":
    urenderer.utils.clear_workdir("03-grandchild")
    renderer = urenderer.renderer.PyplotRenderer(1920, 1080)
    runtime = urenderer.application.Runtime(renderer, name="03-grandchild")

    cube = urenderer.node.Node()
    cube.translation = np.array([0, 0, -5], np.float64)
    cube.rotation = np.array([45, 45, 45], np.float64)
    cube.render_data = urenderer.geometry.polygonal_ifs.get_ifs_cube()
    runtime.scene.add_child(cube)

    child_cube = urenderer.node.Node()
    child_cube.translation = np.array([0, 0, 1], np.float64)
    child_cube.rotation = np.array([0, 0, 0], np.float64)
    child_cube.scale = np.array([0.5, 0.5, 0.5])
    child_cube.render_data = urenderer.geometry.polygonal_ifs.get_ifs_cube()
    cube.add_child(child_cube)

    grandchild_cube = urenderer.node.Node()
    grandchild_cube.translation = np.array([0, 0, 1.5], np.float64)
    grandchild_cube.rotation = np.array([0, 0, 0], np.float64)
    grandchild_cube.scale = np.array([0.25, 0.25, 0.25])
    grandchild_cube.render_data = urenderer.geometry.polygonal_ifs.get_ifs_cube()
    child_cube.add_child(grandchild_cube)

    runtime.iter(capture=True)

    cube.rotation = np.array([45, 90, 45], np.float64)

    runtime.iter(capture=True)
