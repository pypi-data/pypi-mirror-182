from bboxvis import VisCanvas, PViz
import numpy as np

if __name__ == "__main__":
    # a = PViz()

    a = VisCanvas(server=False)
    bbox = np.array([-23.70159063222195, 16.49008742319191, 0.5517544258809011, 3.518475404486515, 1.5305968264604937, 1.7465252991680738, 3.1246051953112426,])
    bbox2 = np.array([-26.157840946004853, 18.46808565785399, 0.5425958214403117, 3.518475404486515, 1.5305968264604937, 1.7465252991680738, 3.1231877554048766])
    pointcloud = np.random.rand(1900, 3)
    a.add_bbox(bbox, color=(0,1,1,1), name='bbox1')
    a.add_bbox(bbox2, color=(1,1,0,1), name='bbox2')
    a.add_pc(pointcloud)
    a.run()
