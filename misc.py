
class Vector(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y


class RCBoundingBox(object):

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        #maximal frame speed
        self.max_frame_bb = 100

    def mid_point(self):
        return (self.x + self.w / 2, self.y + self.h / 2)

    def get_vector(self, bounding_box):
        mid_x, mid_y = self.mid_point()
        prev_mid_x, prev_mid_y = bounding_box.mid_point()
        return Vector(abs(prev_mid_x - mid_x), abs(prev_mid_y - mid_y))
