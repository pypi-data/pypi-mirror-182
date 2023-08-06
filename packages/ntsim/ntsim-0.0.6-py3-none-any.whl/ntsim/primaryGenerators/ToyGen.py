import numpy as np
from ntsim.io.gParticles import gParticles
from ntsim.utils import gen_utils
from ntsim.primaryGenerators.PrimaryGeneratorBase import PrimaryGeneratorBase

class ToyGen(PrimaryGeneratorBase):
    def __init__(self):
        super().__init__('ToyGen')

    def configure(self, opts):
        self.particles = gParticles(1, "primary")
        pdgid = gen_utils.get_pdgid_by_particle_name(opts.toy_primary_name)
        position = opts.position
        time = 0
        direction = opts.toy_primary_direction
        energy = opts.toy_primary_energy
        self.particles.add_particle(pdgid, *position, time, *direction, energy)
        self.log.info('configured')

    def make_event(self, event):
        event.add_particles(self.particles)
