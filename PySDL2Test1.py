import os
os.environ["PYSDL2_DLL_PATH"] = "C:\\SDL2"
import sys
import sdl2.ext

RESOURCES = sdl2.ext.Resources(__file__, "./")

sdl2.ext.init()

window = sdl2.ext.Window("Hello World!", size=(640, 480))
window.show()

factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
sprite = factory.from_image(RESOURCES.get_path("test.png"))

spriterenderer = factory.create_sprite_render_system(window)
spriterenderer.render(sprite)


processor = sdl2.ext.TestEventProcessor()
processor.run(window)



