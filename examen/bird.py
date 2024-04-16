import pygame as pg

class Bird(pg.sprite.Sprite):
    def _init_(self,scale_factor):
        super(Bird,self).__init__()
        self.img_list = [pg.transform.scale_by(pg.image.load("birdup.jpg").convert_alpha(),scale_factor),
                         pg.transform.scale_by(pg.image.load("birddown.jpg").convert_alpha(),scale_factor)]
        self.image_index = 0
        self.image = self.img_list[self.image_index] 
        self.rect = self.image.get_rect(center=(100,100))
        