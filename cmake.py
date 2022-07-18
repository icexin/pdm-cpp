import subprocess
import os.path
import sys


def build(src, dst):
    stage_dir = os.path.join(os.path.dirname(dst), "cmake_build")
    subprocess.run(["conan", "install", src, "--build=missing", "--install-folder=" +
                   stage_dir], check=True, stdout=sys.stdout, stderr=sys.stderr)
    subprocess.run(["cmake", "-S", src, "-B", stage_dir, "-DCMAKE_INSTALL_PREFIX=" +
                   dst], check=True, stdout=sys.stdout, stderr=sys.stderr)
    subprocess.run(["cmake", "--build", stage_dir, "--target", "install"],
                   check=True, stdout=sys.stderr, stderr=sys.stderr)
