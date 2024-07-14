import aframe as af

class AuroraAxiomAR:
    def __init__(self):
        self.scene = af.Scene()

    def add_object(self, object_name, object_position):
        self.scene.append(af.Entity(object_name, position=object_position))

    def render_scene(self):
        return self.scene.html

ar = AuroraAxiomAR()
