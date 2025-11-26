# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *

class SpackExercise(CMakePackage):
    """A simple example package for the Spack exercise."""

    homepage = "https://simulation-software-engineering.github.io/homepage/"
    url = "https://github.com/Simulation-Software-Engineering/spack-exercise/archive/refs/tags/v0.1.0.tar.gz"
    
    # Official repository URL for the main branch
    git = "https://github.com/Simulation-Software-Engineering/spack-exercise.git"

    maintainers("AbdulRehman-Fayyaz")

    version("main", branch="main")
    version("0.3.0", sha256="c179ccc9d56b724fcb7eeff8cebbc1afe2797929b99aa6e7d9b8478a014f2d02")
    version("0.2.0", sha256="010c900a3d4770116844636b89c1e42b1920f27c3da615543fb14f2ae9bb7f64")
    version("0.1.0", sha256="f1c212a58376fd78e9854576627e6927d7cb93ccffe3a162b1664570c491e3a7")

    # Variants for optional dependencies
    variant('boost', default=True, description='Enable Boost support')
    variant('yaml', default=True, description='Enable YAML-CPP support')

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    # Conditional dependencies based on variants
    depends_on("boost@1.65.1:", when="+boost")
    depends_on("yaml-cpp@0.7.0:", when="+yaml")

    # Old versions strictly require Boost/YAML, so we forbid disabling them there
    conflicts("~boost", when="@0.2.0:0.3.0")
    conflicts("~yaml", when="@0.3.0")

    def cmake_args(self):
        args = []
        # Pass flags to CMake based on variants
        args.append(self.define_from_variant("USE_BOOST", "boost"))
        args.append(self.define_from_variant("USE_YAML", "yaml"))
        return args