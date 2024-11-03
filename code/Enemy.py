#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY
from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.Const import WIN_WIDTH, WIN_HEIGHT


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.original_speed = ENTITY_SPEED[self.name]  # Armazena a velocidade original
        self.vertical_speed = -ENTITY_SPEED[self.name]  # Inicialmente movendo para cima

    def move(self):
        # Movimento horizontal
        self.rect.centerx -= ENTITY_SPEED[self.name]

        # Movimento vertical para Enemy3
        if self.name == 'Enemy3':
            # Verifica se a entidade atingiu o limite superior e inverte para baixo
            if self.rect.top <= 0:
                self.vertical_speed = abs(self.vertical_speed) * 2
            # Verifica se a entidade atingiu o limite inferior e inverte para cima
            elif self.rect.bottom >= WIN_HEIGHT:
                self.vertical_speed = -self.original_speed

            # Aplica a velocidade vertical à posição
            self.rect.centery += self.vertical_speed

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
