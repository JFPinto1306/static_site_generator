import os
import shutil

def copy_to_public(dest,src = r'static'):
        # Removing any trees from inside the destination
        if os.path.exists(dest):
                shutil.rmtree(dest)
        
        os.mkdir(dest)
                                
                        
        assert len(os.listdir(dest)) == 0, "Destination directory is not empty"
        
        for path in os.listdir(src):

                src_path = os.path.join(src, path)
                
                if os.path.isfile(src_path):
                        shutil.copy(src_path, dest)
                        continue        
                
                copy_to_public(os.path.join(dest, path), src_path)
                
                        
        return 