#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class LibnameConan(ConanFile):
    name = "elfio"
    version = "3.2"
    description = "Header only ELF reader and producer library"
    url = "https://github.com/Artalus/conan-elfio"
    homepage = "https://github.com/serge1/ELFIO"

    # Indicates License type of the packaged library
    license = "MIT"

    # Packages the license for the conanfile.py
    exports = ["COPYING"]
    settings = "os", "arch", "compiler", "build_type"

    # Custom attributes for Bincrafters recipe conventions
    source_subfolder = "source_subfolder"
    include_subfolder = os.path.join(source_subfolder, "elfio")

    def source(self):
        source_url = self.homepage
        extracted_dir = "ELFIO-Release_"+self.version
        tools.get("{0}/archive/Release_{1}.tar.gz".format(source_url, self.version))

        #Rename to "source_subfolder" is a convention to simplify later steps
        os.rename(extracted_dir, self.source_subfolder)

    def package(self):
        self.copy(pattern="COPYING", dst="licenses", src=self.source_subfolder)
        self.copy(pattern="*", dst="include/elfio", src=self.include_subfolder)

    def package_id(self):
        self.info.header_only()
