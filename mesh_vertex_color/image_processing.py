import math
from PIL import Image, ImageDraw, ImageOps, ImageEnhance

class ImageProcessing():


    def open_image(self, path):
        img = Image.open(path)
        return img


    def export_image(self, img, path):
        img.save(path, quality=100)
        print("Export : {}".format(path))
    

    def create_canvas(self, canvas_size):
        new = Image.new("RGBA", (canvas_size, canvas_size), (0, 0, 0, 0))
        return new


    def change_scale(self, img, target_size):
        img_resize = img.resize((target_size, target_size), Image.LANCZOS)
        return img_resize


    def paste_alpha(self, img0, img1, offset):
        
        c = Image.new('RGBA', img0.size, (0, 0, 0, 0))
        c.paste(img1, offset)

        img_alpha = Image.alpha_composite(img0, c)

        return img_alpha


    def modify_rgb(self, img):

        r, g, b, a = img.split()
        img_new = Image.merge("RGBA", (r, r, b, a))
        return img_new


    def oparete_rgba_channel(self, img):

        r, g, b = img.split()

        img_r = ImageEnhance.Contrast(r)
        rr = img_r.enhance(3)

        ### Blue Canvas
        canvas_size = img.size
        c = Image.new('RGBA', canvas_size, (68, 255, 255, 255))
        cr, cg, cb, ca = c.split()

        img_new = Image.merge("RGBA", (cr, cg, cb, rr))
        
        return img_new


    def image_blend_mask(self, mtrl, mask, mask_flip):
        canvas_size = mask.size
        canvas_new = self.create_canvas(canvas_size[0])

        if mask_flip:
            mask = ImageOps.invert(mask)

        img = Image.composite(canvas_new, mtrl, mask)
        return img

