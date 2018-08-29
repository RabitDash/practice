#include <fstream>
namespace Loader
{
	class Loader
	{
		private:
		string _path;
		fstream _fs;
		public:
			Loader(string path):_path(path)
			{
				_fs.open(_path,ios::in|ios::out|ios::binary);
			}
			~Loader()
			{
				_fs.close();
			}
			void* Read()
			{
				return _fs.read();
			}
	}
}
