ThreeDARD Python Module
*****
Python module to query an fetch the 3D-ARD project.

- Project url: https://3dard.cnrs.fr/
- Dataset url: https://www.archeogrid.fr/project/6762
- Current status: Python API ready for testing. Data can only be downloaded using python module.

.. code-block:: bibtex

    @misc{3dard_2020,
      author = {Mellado, Nicolas and
                Marcadet, Quentin and
                Espinasse, Loic and
                Mora, Pascal and
                Dutailly, Bruno and
                Tournon-Valiente, Sarah and
                Granier, Xavier},
      title = {{3D-ARD}: A 3D-Acquired Research Dataset},
      month = {June},
      year = {2020}
    }


Usage
#####

API usage is demonstrated by two scripts:

 - the Jupyter notebook ``demos/fetchDisplayAndProcess.ipynb``:
 
  - collect and display point clouds and meshes in Jupyter
  - process data using `Open3d <http://www.open3d.org>`_
 -  ``checkDatasetConsistency.py``:
 
  * fetch metadata from server,
  * get file listing for all assets and units in the dataset, check files can be downloaded using the API,
  * print metadatas.


.. code-block:: bash

  $ python3 checkDatasetConsistency.py 

  Processing asset Bone
  [0000] Raw Pictures Bottom (acquisition)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['Nikon 850D, lens Macro TAMRON 90mm, ring light and flash'].
     Description: Set of JPG and NEF pictures
     No details given
  [0001] Raw Pictures Side (acquisition)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['Nikon 850D, lens Macro TAMRON 90mm, ring light and flash'].
     Description: Set of JPG and NEF pictures
     No details given
  [0002] Raw Pictures Unused (acquisition)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['Nikon 850D, lens Macro TAMRON 90mm, ring light and flash'].
     Description: Set of JPG and NEF pictures
     No details given
  [0003] Mask Pictures Bottom (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Software: ['Agisoft Metashape'].
     Description: Set of PNG, mask in alpha to delimited the object
     No details given
     Takes as input ['0000']
  [0004] Mask Pictures Side (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Software: ['Agisoft Metashape'].
     Description: Set of PNG, mask in alpha to delimited the object
     No details given
     Takes as input ['0002']
  [0005] Sparse Point Cloud Side (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Software: ['Agisoft Metashape'].
     Description: Sparse point cloud of the side of the bone. File in .pcd format. Number of points : 296000
     No details given
     Takes as input ['0001']
  [0006] Sparse Point Cloud Bottom (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Software: ['Agisoft Metashape'].
     Description: Sparse point cloud of the bottom of the bone. File in .pcd format. Number of points : 24000
     No details given
     Takes as input ['0000']
  [0007] Sparse Point Cloud All (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Software: ['Agisoft Metashape'].
     Description: Sparse point cloud of the totality of the bone. File in .pcd format. Number of points : 320000
     No details given
     Takes as input ['0005', '0006']
     Is related to ['0000']
  [0008] Dense Point Cloud (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Software: ['Agisoft Metashape'].
     Description: Dense point cloud of the bone. Quality : medium. Filtering mode : aggressive. Number of points : 1,4 million.
     No details given
     Takes as input ['0007']
  [0009] Mesh (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Software: ['Agisoft Metashape'].
     Description: Mesh of the bone in .obj format file. Create with the sparse point cloud. Number of tris : 355000
     No details given
     Takes as input ['0008']

  Processing asset Charango
  [0000] Raw Pictures Top (acquisition)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['Nikon 850D, lens AF-S NIKKOR 24-70mm f/2.8G ED, ring light and flash'].
     Description: Set of JPG and NEF pictures
     No details given
  [0001] Raw Pictures Bottom (acquisition)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['Nikon 850D, lens AF-S NIKKOR 24-70mm f/2.8G ED, ring light and flash'].
     Description: Set of JPG and NEF pictures
     No details given
  [0002] Raw Pictures Unused (acquisition)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['Nikon 850D, lens AF-S NIKKOR 24-70mm f/2.8G ED, ring light and flash'].
     Description: Set of JPG and NEF pictures
     No details given
  [0003] Modified Pictures Top (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['Nikon 850D, lens AF-S NIKKOR 24-70mm f/2.8G ED, ring light and flash'].
     Software: ['Adobe Bridge'].
     Description: Set of JPG pictures, modified to adjust black and white levels
     No details given
     Takes as input ['0000']
  [0004] Modified Pictures Bottom (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['Nikon 850D, lens AF-S NIKKOR 24-70mm f/2.8G ED, ring light and flash'].
     Software: ['Adobe Bridge'].
     Description: Set of JPG pictures, modified to adjust black and white levels
     No details given
     Takes as input ['0001']
  [0005] Modified Pictures Unused (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['Nikon 850D, lens AF-S NIKKOR 24-70mm f/2.8G ED, ring light and flash'].
     Software: ['Adobe Bridge'].
     Description: Set of JPG pictures, modified to adjust black and white levels
     No details given
     Takes as input ['0002']
  [0006] Scan Charango (acquisition)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['HandyScan Creaform'].
     Software: ['Geomagic Wrap'].
     Description: Set of 4 unaligned scans of charango in .ply format file
     Details: 
  [0007] Mesh Scan (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Software: ['Geomagic Wrap'].
     Description: Mesh aligned and not cleaned of scan of charango in .obj format file. Number of tris : 4,33 million
     Details: 
     Takes as input ['0006']
  [0008] Mesh Clean Scan (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Software: ['Metashape Agisoft'].
     Description: Mesh aligned ang cleaned of scan of charango in .obj format file. number of tris : 4,26 million
     Details: 
     Takes as input ['0007']
  [0009] Point Cloud Scan (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Software: ['Geomagic Wrap'].
     Description: Point cloud generate with the aligned and not cleaned mesh of scan of charango in .pcd format file.  
     Details: 
     Takes as input ['0007']
  [0010] Sparse Point Cloud Raw Bottom (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Software: ['Agisoft Metashape '].
     Description: Sparse cloud point of the bottom of the charango and not cleaned in .pcd format file.  
     Details: 
     Takes as input ['0004']
  [0011] Sparse Point Cloud Raw Top (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Software: ['Agisoft Metashape '].
     Description: Sparse cloud point of the top of the charango and not cleaned in .pcd format file.  
     Details: 
     Takes as input ['0003']
  [0012] Dense Point Cloud Clean Bottom (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Software: ['Agisoft Metashape '].
     Description: Dense point cloud of the bottom of the charango cleaned in .pcd format file. Total points : 2,97 million 
     No details given
     Takes as input ['0010']
     Is related to ['0004']
  [0013] Dense Point Cloud Clean Top (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Software: ['Agisoft Metashape '].
     Description: Dense point cloud of the top of the charango cleaned in .pcd format file. Total points : 3,67 million 
     No details given
     Takes as input ['0011']
     Is related to ['0003']
  [0014] Dense Point Cloud Total (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Software: ['Agisoft Metashape '].
     Description: Dense point cloud total of the charango cleaned in .pcd format file. Total points : 6,66 million 
     No details given
     Takes as input ['0012', '0013']
     Is related to ['0011']
  [0015] Mesh (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Software: ['Agisoft Metashape '].
     Description: Mesh of the charango cleaned in .obj format file. Total tris : 9,65 million 
     No details given
     Takes as input ['0014']

  Processing asset Great_tit_skull
  [0000] Raw Pictures Top (acquisition)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['Nikon 850D, lens Macro TAMRON 90mm, ring light and flash'].
     Description: Set of JPG and NEF pictures
     No details given
  [0001] Raw Pictures Bottom (acquisition)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['Nikon 850D, lens Macro TAMRON 90mm, ring light and flash'].
     Description: Set of JPG and NEF pictures
     No details given
  [0002] Raw Pictures Unused (acquisition)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['Nikon 850D, lens Macro TAMRON 90mm, ring light and flash'].
     Description: Set of JPG and NEF pictures
     No details given
  [0003] Modified Pictures Top (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['Nikon 850D, lens Macro TAMRON 90mm, ring light and flash'].
     Software: ['Adobe Bridge'].
     Description: Set of JPG, modified to adjust black and white levels, colors
     No details given
     Takes as input ['0000']
  [0004] Modified Pictures Bottom (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['Nikon 850D, lens Macro TAMRON 90mm, ring light and flash'].
     Software: ['Adobe Bridge'].
     Description: Set of JPG, modified to adjust black and white levels, colors
     No details given
     Takes as input ['0001']
  [0005] Modified Pictures Unused (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['Nikon 850D, lens Macro TAMRON 90mm, ring light and flash'].
     Software: ['Adobe Bridge'].
     Description: Set of JPG, modified to adjust black and white levels, colors
     No details given
     Takes as input ['0002']
  [0006] Scan (process)
     Author: ARTEC
     Description: Final 3D object of mesange skull. Create 5 scans of approx. 4 min. and each comprising approx. 50 photos + some scans (about 20) added for the occluded elements
     Details: 
  [0007] Sparse Point Cloud Top (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Software: ['RealityCapture 1.0.3.4987 RC'].
     Description: Sparse point cloud of the top of the skull, created on RealityCapture. File format .xyz. 
     Details: 
     Takes as input ['0003']
  [0008] Sparse Point Cloud Bottom (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Software: ['RealityCapture 1.0.3.4987 RC'].
     Description: Sparse point cloud of the bottom of the skull, created on RaelityCapture. File format .xyz. 
     Details: 
     Takes as input ['0004']
  [0009] Sparse Point Cloud Total (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Software: ['RealityCapture 1.0.3.4987 RC'].
     Description: Sparse point cloud create on RaelityCapture with sparse point cloud top and bottom merged. File format .xyz. 
     Details: 
     Takes as input ['0007', '0008']
  [0010] Mesh (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Software: ['RealityCapture 1.0.3.4987 RC'].
     Description: Mesh created on RaelityCapture with the sparse cloud point total. File format .obj with approx. 8,9 millions tris
     No details given
     Takes as input ['0009']

  Processing asset Haut_Carre
  [0000] Raw Pictures Exterior (acquisition)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['Nikon 850D, lens AF-S NIKKOR 24-70mm f/2.8G ED'].
     Description: Set of JPG and NEF pictures. Exterior of the annexe building
     No details given
  [0001] Raw Pictures Exterior Drone (acquisition)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['DJI Inspire 2, lens 15mm'].
     Description: Set of JPG, DNG and xmp pictures. Exterior with drone of the annexe building
     No details given
  [0002] Raw Pictures Interior (acquisition)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['Nikon 850D, lens AF-S NIKKOR 24-70mm f/2.8G ED and flash ring'].
     Description: Set of JPG and NEF pictures. Interior of the annexe building
     No details given
  [0003] Modified Pictures Exterior (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['Nikon 850D, lens AF-S NIKKOR 24-70mm f/2.8G ED'].
     Software: ['Adobe Bridge'].
     Description: Set of JPG pictures, modified to adjust black and white level. Exterior ofthe annex building
     No details given
     Takes as input ['0000']
  [0004] Modified Pictures Interior (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['Nikon 850D, lens AF-S NIKKOR 24-70mm f/2.8G ED and flash ring'].
     Software: ['Adobe Bridge'].
     Description: Set of JPG pictures, modified to adjust black and white level. Interior of the annex building
     No details given
     Takes as input ['0002']
  [0005] Scans Totality Annex Building E57 (acquisition)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['Leica RTC360'].
     Software: ['Cyclone Register 360'].
     Description: Set of .e57 of the totality of the annex building. Exterior and interior
     No details given
  [0006] Scans Totality Frame E57 (acquisition)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['Leica RTC360'].
     Software: ['Cyclone Register 360'].
     Description: Set of .e57 of the totality of the wood frame.
     No details given
  [0007] Scans Totality Annex Building PTX (acquisition)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['Leica RTC360'].
     Software: ['Cyclone Register 360'].
     Description: Set of .ptx of the totality of the annex building. Exterior and interior
     No details given
  [0008] Scans Totality Frame E57 (acquisition)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['Leica RTC360'].
     Software: ['Cyclone Register 360'].
     Description: Set of .ptx of the totality of the wood frame.
     No details given
  [0009] Dense Point Cloud Top (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Software: ['Agisoft Metashape 1.6.0 build 9925'].
     Description: Dense point cloud of the top of the annex building in .pcd format file. Total points : 469 million. 
     No details given
     Takes as input ['0001']
  [0010] Dense Point Cloud Bottom (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Software: ['Agisoft Metashape 1.6.0 build 9925'].
     Description: Dense point cloud of the bottom of the annex building in .pcd format file. Total points : 94 million. 
     No details given
     Takes as input ['0000']
  [0011] Dense Point Cloud Total (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Software: ['Agisoft Metashape 1.6.0 build 9925'].
     Description: Dense point cloud of the totality of the annex building in .pcd format file. Created with the merge of the top and bottom dense cloud. Cleaned version. Total points : 368,5 million. 
     No details given
     Takes as input ['0009', '0010']
     Is related to ['0000']
  [0012] Mesh (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Software: ['Agisoft Metashape 1.6.0 build 9925'].
     Description: Mesh of the annex building in .obj format file. Created with the depth map mode. Cleaned version. Total tris : 126,1 million. 
     No details given

  Processing asset Junk_ship
  [0000] Raw Pictures Top (acquisition)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['Nikon 850D, lens AF-S NIKKOR 24-70mm f/2.8G ED, ring light and flash'].
     Description: Set of JPG and NEF pictures
     No details given
  [0001] Raw Pictures Left (acquisition)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['Nikon 850D, lens AF-S NIKKOR 24-70mm f/2.8G ED, ring light and flash'].
     Description: Set of JPG and NEF pictures
     No details given
  [0002] Raw Pictures Right (acquisition)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['Nikon 850D, lens AF-S NIKKOR 24-70mm f/2.8G ED, ring light and flash'].
     Description: Set of JPG and NEF pictures
     No details given
  [0003] Raw Pictures Unused (acquisition)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['Nikon 850D, lens AF-S NIKKOR 24-70mm f/2.8G ED, ring light and flash'].
     Description: Set of JPG and NEF pictures
     No details given
  [0004] Modified Pictures Top (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['Nikon 850D, lens AF-S NIKKOR 24-70mm f/2.8G ED, ring light and flash'].
     Software: ['Adobe Bridge'].
     Description: Set of JPG pictures, modified to adjust black and white levels
     No details given
     Takes as input ['0000']
  [0005] Modified Pictures Left (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['Nikon 850D, lens AF-S NIKKOR 24-70mm f/2.8G ED, ring light and flash'].
     Software: ['Adobe Bridge'].
     Description: Set of JPG pictures, modified to adjust black and white levels
     No details given
     Takes as input ['0001']
  [0006] Modified Pictures Right (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['Nikon 850D, lens AF-S NIKKOR 24-70mm f/2.8G ED, ring light and flash'].
     Software: ['Adobe Bridge'].
     Description: Set of JPG pictures, modified to adjust black and white levels
     No details given
     Takes as input ['0002']
  [0007] Modified Pictures Unused (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['Nikon 850D, lens AF-S NIKKOR 24-70mm f/2.8G ED, ring light and flash'].
     Software: ['Adobe Bridge'].
     Description: Set of JPG pictures, modified to adjust black and white levels
     No details given
     Takes as input ['0003']
  [0008] Scans (acquisition)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['HandyScan Creaform'].
     Description: Set of 4 scans unaligned of the differents parts of the junk in .ply format
     Details: 
  [0009] Point Cloud Scan (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Software: ['Geomagic Wrap'].
     Description: Point cloud generate with the aligned and cleaned mesh of scan of junk in .pcd format file. Number of points : 5 million
     Details: 
     Takes as input ['0008']
  [0010] Mesh Scan (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Software: ['Geomagic Wrap'].
     Description: Mesh aligned of scan of junk in .obj format file. Number of tris : 10 million
     Details: 
     Takes as input ['0009']
  [0011] Sparse Point Cloud Top (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Software: ['Reality Capture'].
     Description: Sparse point cloud of the top part of the junk. File in .xyz format
     No details given
     Takes as input ['0004']
  [0012] Sparse Point Cloud Left (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Software: ['Reality Capture'].
     Description: Sparse point cloud of the left part of the junk. File in .xyz format
     No details given
     Takes as input ['0005']
  [0013] Sparse Point Cloud Right (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Software: ['Reality Capture'].
     Description: Sparse point cloud of the right part of the junk. File in .xyz format
     No details given
     Takes as input ['0006']
  [0014] Sparse Point Cloud Total (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Software: ['Reality Capture'].
     Description: Sparse point cloud in raw version of the junk. File in .xyz format
     No details given
     Takes as input ['0011', '0012', '0013']
     Is related to ['0006']
  [0015] Mesh (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Software: ['Reality Capture'].
     Description: Mesh of the totality of the junk reconstructed and textured with the top, left, and right parts, without elements around. File in .obj format for mesh, and png format for the texture
     No details given
     Takes as input ['0014']

  Processing asset Lady_of_Elche
  [0000] Raw Pictures (acquisition)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['Nikon 850D, lens AF-S NIKKOR 24-70mm f/2.8G ED, ring light and flash'].
     Description: Set of JPG and NEF pictures
     No details given
  [0001] Modified Pictures (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['Nikon 850D, lens AF-S NIKKOR 24-70mm f/2.8G ED, ring light and flash'].
     Software: ['Photoshop'].
     Description: Set of JPG pictures, modified to adjust black and white levels
     No details given
     Takes as input ['0000']
  [0002] Dense Point Cloud (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Software: ['Agisoft Metashape 1.6.2.10247'].
     Description: High and medium dense cloud points. High : 84,8 million points. Medium : 36,7 million points.
     No details given
     Takes as input ['0001']
  [0003] Mesh (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Software: ['Agisoft Metashape 1.6.2.10247'].
     Description: High and medium mesh. High : 16,6 million tris. Medium : 653000 tris.
     No details given
     Takes as input ['0002']
  [0004] Scan Front (acquisition)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['FaroArm PLatinium'].
     Software: ['Geomagic Wrap'].
     Description: Set of points clouds for front view of Lady of Elche
     No details given
     Is related to []
  [0005] Scan Back (acquisition)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['FaroArm PLatinium'].
     Software: ['Geomagic Wrap'].
     Description: Set of points clouds for back view of Lady of Elche
     No details given
     Is related to []
  [0006] Scan Left (acquisition)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['FaroArm PLatinium'].
     Software: ['Geomagic Wrap'].
     Description: Set of points clouds for left view of Lady of Elche
     No details given
     Is related to []
  [0007] Scan Right (acquisition)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['FaroArm PLatinium'].
     Software: ['Geomagic Wrap'].
     Description: Set of points clouds for right view of Lady of Elche
     No details given
     Is related to []
  [0008] Scan Top (acquisition)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['FaroArm PLatinium'].
     Software: ['Geomagic Wrap'].
     Description: Set of points clouds for top view of Lady of Elche
     No details given
     Is related to []
  [0009] Scan Point Cloud (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Software: ['Geomagic Wrap 2017 '].
     Description: Point cloud in raw format with 2,2 million points
     No details given
     Takes as input ['0004', '0005', '0006', '0007', '0008']
     Is related to []
  [0010] Mesh Scan (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Software: ['Geomagic Wrap 2017 '].
     Description: Set of scans with raw format, decimate mesh and mesh with holes closed
     No details given
     Takes as input ['0009']

  Processing asset Maitreya_Buddha
  [0000] Raw Pictures Top (acquisition)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['Nikon 850D, lens AF-S NIKKOR 24-70mm f/2.8G ED, ring light and flash'].
     Description: Set of JPG and NEF pictures
     No details given
  [0001] Raw Pictures Bottom (acquisition)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['Nikon 850D, lens AF-S NIKKOR 24-70mm f/2.8G ED, ring light and flash'].
     Description: Set of JPG and NEF pictures
     No details given
  [0002] Raw Pictures Unused (acquisition)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['Nikon 850D, lens AF-S NIKKOR 24-70mm f/2.8G ED, ring light and flash'].
     Description: Set of JPG and NEF pictures
     No details given
  [0003] Modified Pictures Top (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['Nikon 850D, lens AF-S NIKKOR 24-70mm f/2.8G ED, ring light and flash'].
     Description: Set of JPG, modified to adjust black and white levels, colors
     No details given
     Takes as input ['0000']
  [0004] Modified Pictures Bottom (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['Nikon 850D, lens AF-S NIKKOR 24-70mm f/2.8G ED, ring light and flash'].
     Description: Set of JPG, modified to adjust black and white levels, colors
     No details given
     Takes as input ['0001']
  [0005] Modified Pictures Unused (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['Nikon 850D, lens AF-S NIKKOR 24-70mm f/2.8G ED, ring light and flash'].
     Description: Set of JPG, modified to adjust black and white levels, colors
     No details given
     Takes as input ['0002']
  [0006] Scans (acquisition)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['HandyScan Creaform'].
     Software: ['Geomagic Wrap'].
     Description: Set of 3 unaligned scans of Maitreya Buddha Statue in .ply format file with their text files containing point coordinates
     Details: 
  [0007] Mesh Scan (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['HandyScan Creaform'].
     Software: ['Geomagic Wrap'].
     Description: Mesh aligned and cleaned of scan of charango in .obj format file. Number of tris : 8 million
     Details: 
     Takes as input ['0006']
  [0008] Point Cloud Scan (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Hardware: ['HandyScan Creaform'].
     Software: ['Geomagic Wrap'].
     Description: Point cloud generate with the aligned and cleaned mesh of scan of charango in .pcd format file.
     Details: 
     Takes as input ['0007']
  [0009] Sparse Point Cloud Top (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Software: ['Agisoft Metashape'].
     Description: Sparse point cloud top of the Maitreya Buddha. File in .pcd format. Number of points : 1,17 million
     No details given
     Takes as input ['0003']
  [0010] Sparse Point Cloud Bottom (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Software: ['Agisoft Metashape'].
     Description: Sparse point cloud bottom of the Maitreya Buddha. File in .pcd format. Number of points : 56000
     No details given
     Takes as input ['0004']
  [0011] Sparse Point Cloud All (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Software: ['Agisoft Metashape'].
     Description: Total sparse point cloud of the Maitreya Buddha. File in .pcd format. Number of points : 1,3 million
     No details given
     Takes as input ['0009', '0010']
     Is related to ['0004']
  [0012] Dense Point Cloud (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Software: ['Agisoft Metashape'].
     Description: Dense point cloud not cleaned of the Maitreya Buddha. File in .pcd format. Number of points : 22,65 million
     Details: 
     Takes as input ['0011']
  [0013] Mesh (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Software: ['Agisoft Metashape'].
     Description: Mesh with texture of the Maitreya Buddha. File in .obj format. Number of tris : 4,5 million.
     No details given
     Takes as input ['0011']
  [0014] Mesh Decimated (process)
     Author: MARCADET Quentin <quentin.marcadet@gmail.com>
     Software: ['Agisoft Metashape'].
     Description: Mesh decimated with texture of the Maitreya Buddha. File in .obj format. Number of tris : 50000
     No details given
     Takes as input ['0013']
