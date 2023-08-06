
import pyscreenshot as ImageGrab


if __name__ == '__main__':
    # wx2 = wx.App()  # Need to create an App instance before doing anything
    # screen = wx.ScreenDC()
    # size = screen.GetSize()
    # bmp = wx.EmptyBitmap(size[0], size[1])
    # mem = wx.MemoryDC(bmp)
    # mem.Blit(0, 0, size[0], size[1], screen, 0, 0)
    # del mem  # Release bitmap
    # bmp.SaveFile('screenshot.png', wx.BITMAP_TYPE_PNG)
    # taking_screenshot()
    # grab fullscreen
    im = ImageGrab.grab()

    # save image file
    im.save("fullscreen.png")