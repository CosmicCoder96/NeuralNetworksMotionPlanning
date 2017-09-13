import pygame
import math
from PodSixNet.Connection import ConnectionListener, connection
WHITE = (255, 255, 255)

class Car(pygame.sprite.Sprite):
    def __init__(self, img, location):
        super().__init__()
        self.image = pygame.image.load(img).convert()
        self.cleanImage = self.image.copy()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.width=self.rect.width
        self.height=self.rect.height
        self.geometricangle=math.atan(self.width/self.height)
        self.rect.topleft = location
        self.topleft=self.rect.topleft
        self.bottomleft=self.rect.bottomleft
        self.topright=self.rect.topright
        self.cornersensor=math.hypot(self.rect.centerx - self.topright[0], self.rect.centery - self.topright[1])
        self.bottomright=self.rect.bottomright
        self.screen=pygame.display.get_surface()
        self.currentAngle = 0
    def updateSensors(self):
        # print(self.width, self.height)

        self.bottomright=(self.rect.centerx + self.cornersensor*math.sin(math.radians(self.currentAngle)+self.geometricangle) ,self.rect.centery+self.cornersensor*math.cos(math.radians(self.currentAngle)+self.geometricangle))
        # self.bottomleft=(self.rect.centerx - self.cornersensor*math.sin(math.radians(self.currentAngle)+self.geometricangle) ,self.rect.centery+self.cornersensor*math.cos(math.radians(self.currentAngle)+self.geometricangle))
        # print(5)
    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def moveForward(self, pixels):
        print(self.currentAngle, math.sin(math.radians(self.currentAngle)), math.cos(math.radians(self.currentAngle)))
        self.rect.x += pixels*math.cos(math.radians(self.currentAngle))
        self.rect.y -= pixels*math.sin(math.radians(self.currentAngle))
        print (self.rect.topright)


    def moveBackward(self, pixels):
        print(self.currentAngle, math.sin(math.radians(self.currentAngle)), math.cos(math.radians(self.currentAngle)))
        self.rect.x -= pixels * math.cos(math.radians(self.currentAngle))
        self.rect.y += pixels * math.sin(math.radians(self.currentAngle))
        print (self.rect.topright)


    def rotateLeft(self, angle):
        self.currentAngle += angle
        self.currentAngle%=360
        self.image, self.rect = self.rot_center(self.cleanImage, self.rect, self.currentAngle)

    def rot_center(self, image, rect, angle):
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = rot_image.get_rect(center=rect.center)
        return rot_image, rot_rect

    def rotateRight(self, angle):
        self.currentAngle-=angle
        self.currentAngle%=360
        self.image, self.rect=self.rot_center(self.cleanImage, self.rect, self.currentAngle)









