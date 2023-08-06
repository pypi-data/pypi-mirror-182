import pygame
import sys,os

class ImageLibrary():
    """ImageLibrary is a class that stores the images loaded by the PyGineGame class, and is used to access them"""
    images = {}
    def __init__(self,assetFolder="Assets"):
        """Constructor for ImageLibrary"""
        print()
        assert assetFolder != "", "You must specify an asset folder"
        #fint the root folder

        root = os.path.dirname(os.path.abspath(__file__))
        self.LoadAllImages(sys.path[1]+"/"+assetFolder.removesuffix("/").removeprefix("/"))

    def LoadAllImages(self, path):
        """Load all the images in a folder"""

        for file in os.listdir(path):
            if file.endswith(".png"):
                self.addImage(file, path +"/"+ file)

    def addImage(self, name, path):
        """Add an image to the library, with a name and a path"""
        ImageLibrary.images[name] = pygame.image.load(path).convert()
        #scale the image to a constant
        ImageLibrary.images[name] = pygame.transform.scale(self.images[name], (100,100))
        ImageLibrary.images[name].set_colorkey((255,255,255))
        ImageLibrary.images[name].convert_alpha()

    def getImage(self, name):
        """Get an image from the library, with a name"""
        if name in ImageLibrary.images:
            return ImageLibrary.images[name]
        else:
            return ImageLibrary.images["default"]

    def removeImage(self, name):
        """Remove an image from the library, with a name"""
        if name in ImageLibrary.images:
            del ImageLibrary.images[name]

    def listImages(self):
        """List all the images in the library"""
        for key in ImageLibrary.images:
            print(key)

    def clear(self):
        """Clear the library"""
        ImageLibrary.images = {}
        ImageLibrary.images["default"] = pygame.image.load("PyGine/DefaultImage.png")
        ImageLibrary.images["default"] = pygame.transform.scale(self.images["default"], (100,100))
        ImageLibrary.images["default"].set_colorkey((255,255,255))
        ImageLibrary.images["default"].convert_alpha()