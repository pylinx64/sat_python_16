from mcpi.minecraft import Minecraft
# сервер
mc = Minecraft.create()

# собираем координаты игрока 
pos = mc.player.getTilePos()

x=pos.x
y=pos.y
z=pos.z
block=46
block_1=152

# ставит блок
mc.setBlock(x, y, z, block)
mc.setBlock(x, y+1, z, block_1)
