"""
    Module to handle cloning a private repo on github
"""
import os
import shutil
import git

def clone_private_pkg(pkg_url,pat='',path='/content'):
  # Clone package and ensure path is added to sys directory
  pkg_name = pkg_url.split('/')[-1].split('.')[0]
  pkg_path = os.path.join(path,pkg_name)

  # check if a folder for the package already exist, if it does remove it, then perform clone of pkg
  if os.path.exists(pkg_path):
    shutil.rmtree(pkg_path,ignore_errors=False,onerror=None)
    print(f"Old {pkg_name} package removed successfully")

  # if package does not exist then can perform a clone
  try:
    url = pkg_url.split("//")
    pat_insert = f"//{pat}@"
    url.insert(1,pat_insert)
    updated_url = "".join(url)
    print(updated_url)
    git.Repo.clone_from(updated_url,pkg_path,branch='master')
    print(f"New {pkg_name} package downloaded")
  except:
    print(f"Error cloning {pkg_name} package - double check PAT and Pkg URL")
    return False #if pkg can't be installed, will exit and return false

  # check if old pkg reference in sys path, if is then remove it, then add new one
  print("Updating sys paths")
  if pkg_path in os.sys.path:
      os.sys.path.remove(pkg_path)
  os.sys.path.append(pkg_path)

  print(f"{pkg_name} Package ready to be imported!")
  return True

def clone_public_pkg(pkg_url,pat='',path='/content'):
  pass
