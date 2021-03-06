#include <KrisLibrary/geometry/TSDFReconstruction.h>
#include <KrisLibrary/meshing/IO.h>
#include <Klampt/Modeling/World.h>
#include <KrisLibrary/GLdraw/GLUTNavigationProgram.h>
#include <KrisLibrary/GLdraw/drawextra.h>
#include <KrisLibrary/GLdraw/GLRenderToImage.h>
#include <GL/gl.h>
#include <string.h>
using namespace Geometry;
using namespace Meshing;
using namespace std;
using namespace GLDraw; 

const int num_pcd = 5;

int main(int argc,char** argv)
{
	//load first point cloud
	PointCloud3D pc;
	const char* fn1 = "experiment_data/tmp/processed/objectScan_0.pcd";
	//char* fn1 = "../pcd_data/objectScan_0.pcd";
	bool res;
	res = pc.LoadPCL(fn1);
	bool hasColor;
	hasColor = pc.HasColor();
	if (res) cout << "----- Load first scan success -----" << hasColor << "\n";
	

	//initialize the identity transform
	double Rotation[3][3]= {1.0,0,0,0,1.0,0,0,0,1.0};//{{1.0,0,0},{0,1.0,0},{0,0,1.0}};
	Matrix3 R(Rotation);
	Vector3 translation1(0,0,0);
	Vector3 translation2(0,0.0005,0);
	RigidTransform Tcamera1(R,translation1);//identity transformation
	RigidTransform Tcamera2(R,translation2);
		
	//Initialize TSDF and fuse first pcd
	/* This way is from the TSDF test.cpp, but fuse gives segfault..
	shared_ptr<SparseTSDFReconstruction> reconstruction;
	reconstruction->Fuse(Tcamera1,pc);
	TriMesh mesh;
	reconstruction -> ExtractMesh(mesh);
	*/

	Vector3 cellSize = {0.0006,0.0006,0.001};
	Vector3 cellSize2 = {0.001,0.001,0.001};
	SparseTSDFReconstruction reconstruction(cellSize); //use this to perform ICP
	SparseTSDFReconstruction reconstruction2(cellSize2); //less dense.
	RigidTransform Tcamera = Tcamera1;
	reconstruction.Fuse(Tcamera,pc);
	reconstruction2.Fuse(Tcamera,pc);

	// really bad code.... but I'm not sure how to concatenate char, and whether
	// pc.loadPCL will remove the existing pcl...
	for(int i=1 ;i<5;i++)
	{
		string fn = "experiment_data/tmp/processed/objectScan_"+to_string(i)+".pcd";
		PointCloud3D pc;
		pc.LoadPCL(fn.c_str());
		ICPParameters params;
		reconstruction.Register(pc,Tcamera,params);
		cout<<params.Tcamera<<endl;
		//reconstruction.Fuse(Tcamera1,pc);
		Tcamera = params.Tcamera;
		reconstruction.Fuse(Tcamera,pc);
		reconstruction2.Fuse(Tcamera,pc);
		cout<<i<<endl;
	}

	//Extract a colored mesh
	GeometryAppearance app;
	TriMesh mesh;
	reconstruction2.ExtractMesh(mesh,app);
	//app.SetColor(1.0f,0.2f,0.2f,0.5f);
	const char* fn0 = "experiment_data/tmp/TSDF_result.ply"; // ply format seems to be the only
										// cross section between Assimp and Open3D....	
	//cout << "flag1\n" ;
	//cout << "done\n" ;
	//res = Export(fn2,mesh,app);
	res = SaveAssimp(fn0,mesh,app);
	if (res) cout << "----- Extracted mesh exported -----" << "\n";
	
	// simply saving the mesh by: mesh.Save(fn2); does not work... this saves 
	// it as a TriMesh file....
	return 0;

	/*
	// load and fuse multiple pcs

	//reconstruction -> Fuse(Tcamera2,pc)
	*/
}
