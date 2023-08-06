import os.path
from datetime import datetime, timedelta

today_date = datetime.today().date()


class IndexExecuter:
    def __init__(self, output_dir_path='tmp'):
        from unsupcc.satellite import sentinel2
        from unsupcc.satellite import indices
        self.start_date = input('Enter Start date in yyyy-mm-dd format: ') or str(today_date - timedelta(90))
        self.end_date = input('Enter End date in yyyy-mm-dd format: ') or str(today_date)
        self.indice_name = input('Enter target indice name for crop classification eg: ndvi / fcc: ') or 'ndvi'
        self.cloud_threshold = int(input('Enter cloud threshold in percentage for sentinel 2 tiles: ') or 10)
        self.data_interval = int(input('Enter Number of days interval for sentinel2 data & indice ts:') or 15)
        self.shape_file_path = input('provide complete path of shapefile, Skip if passing bbox') or None
        self.bbox = input('provide valid bounding box in order - minx miny maxx maxy! Skip if '
                          'passing shapefile') or None
        self.width = input('Enter width of array if input is raster or bbox: ') or None
        self.height = None
        if self.width:
            self.width = int(self.width)
            self.height = int(input('Enter height of array:'))
        self.output_dir_path = output_dir_path
        self.s2 = sentinel2.Sentinel2()
        self.idc = indices.indice()

    def get_layer_stack(self):
        if self.shape_file_path:
            self.shape_file_path = self.shape_file_path.replace('\\', '/')
        bounds = None
        if self.bbox:
            bounds = tuple(float(item) for item in self.bbox.split(' '))
        return self.idc.layer_stack(self.start_date, self.end_date, self.cloud_threshold, self.data_interval,
                                    self.indice_name, self.shape_file_path, bounds, self.width, self.height)


class ClusterExecuter:
    def __init__(self, output_dir_path='tmp'):
        from unsupcc.classification import crop_classifier
        self.output_dir_path = output_dir_path
        self.cc = crop_classifier.Classifier()
        # self.layer_stack_path = input('provide complete path of ndvi/fcc stack:  ') or \
        #                         os.path.join(output_dir_path, 'stack', 'ndvi.tif')
        # self.date_band_ids = input('provide space separated band ids wrt selected dates from ndvi/fcc '
        #                         'stack (space separated):  ')

    def kmeans_cluster(self, layer_stack_path, date_band_ids, number_of_cluster=None, number_of_crop=None):
        return self.cc.crop_cluster(layer_stack_path, date_band_ids, number_of_cluster, number_of_crop)
