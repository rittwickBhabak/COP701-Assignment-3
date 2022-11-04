from tkinter import Image, PhotoImage
from tkinter import _default_root, _cnfmerge, TclError



class OfficialImage:
    """Base class for images."""
    _last_id = 0
    def __init__(self, imgtype, name=None, cnf={}, master=None, **kw):
        self.name = None
        print(cnf)
        print("----------------------------------")
        print(kw)
        if not master:
            master = _default_root
            if not master:
                raise RuntimeError('Too early to create image')
        self.tk = getattr(master, 'tk', master)
        if not name:
            Image._last_id += 1
            name = "pyimage%r" % (Image._last_id,) # tk itself would use image<x>
        if kw and cnf: cnf = _cnfmerge((cnf, kw))
        elif kw: cnf = kw
        options = ()
        for k, v in cnf.items():
            if callable(v):
                v = self._register(v)
            options = options + ('-'+k, v)
        self.tk.call(('image', 'create', imgtype, name,) + options)
        self.name = name
    def __str__(self): return self.name
    def __del__(self):
        if self.name:
            try:
                self.tk.call('image', 'delete', self.name)
            except TclError:
                # May happen if the root was destroyed
                pass
    def __setitem__(self, key, value):
        self.tk.call(self.name, 'configure', '-'+key, value)
    def __getitem__(self, key):
        return self.tk.call(self.name, 'configure', '-'+key)
    def configure(self, **kw):
        """Configure the image."""
        res = ()
        for k, v in _cnfmerge(kw).items():
            if v is not None:
                if k[-1] == '_': k = k[:-1]
                if callable(v):
                    v = self._register(v)
                res = res + ('-'+k, v)
        self.tk.call((self.name, 'config') + res)
    config = configure
    def height(self):
        """Return the height of the image."""
        return self.tk.getint(
            self.tk.call('image', 'height', self.name))
    def type(self):
        """Return the type of the image, e.g. "photo" or "bitmap"."""
        return self.tk.call('image', 'type', self.name)
    def width(self):
        """Return the width of the image."""
        return self.tk.getint(
            self.tk.call('image', 'width', self.name))

class OfficialPhotoImage(OfficialImage):
    """Widget which can display images in PGM, PPM, GIF, PNG format."""
    def __init__(self, name=None, cnf={}, master=None, **kw):
        """Create an image with NAME.

        Valid resource names: data, format, file, gamma, height, palette,
        width."""
        OfficialImage.__init__(self, 'photo', name, cnf, master, **kw)
    def blank(self):
        """Display a transparent image."""
        self.tk.call(self.name, 'blank')
    def cget(self, option):
        """Return the value of OPTION."""
        return self.tk.call(self.name, 'cget', '-' + option)
    # XXX config
    def __getitem__(self, key):
        return self.tk.call(self.name, 'cget', '-' + key)
    # XXX copy -from, -to, ...?
    def copy(self):
        """Return a new PhotoImage with the same image as this widget."""
        destImage = PhotoImage(master=self.tk)
        self.tk.call(destImage, 'copy', self.name)
        return destImage
    def zoom(self, x, y=''):
        """Return a new PhotoImage with the same image as this widget
        but zoom it with a factor of x in the X direction and y in the Y
        direction.  If y is not given, the default value is the same as x.
        """
        destImage = PhotoImage(master=self.tk)
        if y=='': y=x
        self.tk.call(destImage, 'copy', self.name, '-zoom',x,y)
        return destImage
    def subsample(self, x, y=''):
        """Return a new PhotoImage based on the same image as this widget
        but use only every Xth or Yth pixel.  If y is not given, the
        default value is the same as x.
        """
        destImage = PhotoImage(master=self.tk)
        if y=='': y=x
        self.tk.call(destImage, 'copy', self.name, '-subsample',x,y)
        return destImage
    def get(self, x, y):
        """Return the color (red, green, blue) of the pixel at X,Y."""
        return self.tk.call(self.name, 'get', x, y)
    def put(self, data, to=None):
        """Put row formatted colors to image starting from
        position TO, e.g. image.put("{red green} {blue yellow}", to=(4,6))"""
        args = (self.name, 'put', data)
        if to:
            if to[0] == '-to':
                to = to[1:]
            args = args + ('-to',) + tuple(to)
        self.tk.call(args)
    # XXX read
    def write(self, filename, format=None, from_coords=None):
        """Write image to file FILENAME in FORMAT starting from
        position FROM_COORDS."""
        args = (self.name, 'write', filename)
        if format:
            args = args + ('-format', format)
        if from_coords:
            args = args + ('-from',) + tuple(from_coords)
        self.tk.call(args)
