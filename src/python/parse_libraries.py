import ast
import inspect
import os

def create_test_file(full_file_name, class_name="S3FileManager",sufix_class="_01", sufix_methods="_01"):
    str_code = f"""
import os
from boto.s3.connection import S3Connection
from boto.s3.key import Key


def downloadFile{sufix_methods}(s3_file, local_download_destination):
    full_local_path = os.path.expanduser(os.path.join(local_download_destination, s3_file.name))
    try:
        print("Downloaded: {{0}}".format(full_local_path))
        s3_file.get_contents_to_filename(full_local_path)
    except:
        print("Error downloading")


def deleteFile{sufix_methods}(bucket, s3_file):
        bucket.delete_key(s3_file)
        print("Deleted: {{0}}".format(s3_file.name))


class {class_name}{sufix_class}:

    def __init__(self, aws_key, aws_secret, use_ssl):
        self._aws_connection = S3Connection(aws_key, aws_secret, is_secure = use_ssl)

    def getFileNamesInBucket{sufix_methods}(self, aws_bucketname):
        if not self._bucketExists{sufix_methods}(aws_bucketname):
            self._printBucketNotFoundMessage{sufix_methods}(aws_bucketname)
            return list()
        else:
            bucket = self._aws_connection.get_bucket(aws_bucketname)
            return map(lambda aws_file_key: aws_file_key.name, bucket.list())

    def downloadFileFromBucket{sufix_methods}(self, aws_bucketname, filename, local_download_directory):
        if not self._bucketExists{sufix_methods}(aws_bucketname):
            self._printBucketNotFoundMessage{sufix_methods}(aws_bucketname)
        else:
            bucket = self._aws_connection.get_bucket(aws_bucketname)
            for s3_file in bucket.list():
                if filename == s3_file.name:
                    downloadFile{sufix_methods}(s3_file, local_download_directory)
                    break;

    def downloadAllFilesFromBucket{sufix_methods}(self, aws_bucketname, local_download_directory):
        if not self._bucketExists{sufix_methods}(aws_bucketname):
            self._printBucketNotFoundMessage{sufix_methods}(aws_bucketname)
        else:
            bucket = self._aws_connection.get_bucket(aws_bucketname)
            for s3_file in bucket.list():
                downloadFile{sufix_methods}(s3_file, local_download_directory)

    def deleteAllFilesFromBucket{sufix_methods}(self, aws_bucketname):
        if not self._bucketExists{sufix_methods}(aws_bucketname):
            self._printBucketNotFoundMessage{sufix_methods}(aws_bucketname)
        else:
            bucket = self._aws_connection.get_bucket{sufix_methods}(aws_bucketname)
            for s3_file in bucket.list():
                deleteFile{sufix_methods}(bucket, s3_file)

    def downloadFilesInBucketWithPredicate{sufix_methods}(self, aws_bucketname, filename_predicate, local_download_destination):
        if not self._bucketExists{sufix_methods}(aws_bucketname):
            self._printBucketNotFoundMessage{sufix_methods}(aws_bucketname)
        else:
            bucket = self._aws_connection.get_bucket(aws_bucketname)
            for s3_file in filter(lambda fkey: filename_predicate(fkey.name), bucket.list()):
                downloadFile{sufix_methods}(s3_file, local_download_destination)

    def deleteFilesInBucketWithPredicate{sufix_methods}(self, aws_bucketname, filename_predicate):
        if not self._bucketExists{sufix_methods}(aws_bucketname):
            self._printBucketNotFoundMessage{sufix_methods}(aws_bucketname)
        else:
            bucket = self._aws_connection.get_bucket(aws_bucketname)
            for s3_file in filter(lambda fkey: filename_predicate(fkey.name), bucket.list()):
                deleteFile{sufix_methods}(bucket, s3_file)

    def _bucketExists{sufix_methods}(self, bucket_name):
        return self._aws_connection.lookup(bucket_name) != None

    def _printBucketNotFoundMessage{sufix_methods}(self, bucket_name):
        print("Error: bucket '{{0}}' not found".format(bucket_name))

    """
    # print(str_code)
    if full_file_name:
        file_ptr = open(full_file_name, 'w+')
        file_ptr.write(str_code) 
        file_ptr.close()


def create_test_file_import_level(
            full_file_name, 
            current_level, 
            class_name="S3FileManagerClient",
            sufix_class="_01", 
            sufix_methods="_01"):
    """
    
    """
    module_level = "TBD"
    str_code = f"""
import os
from {module_level} import Key
from {module_level} import downloadFile


def dummy_function{sufix_methods}(s3_file, local_download_destination):
    full_local_path = os.path.expanduser(os.path.join(local_download_destination, s3_file.name))
    try:
        print("Downloaded: {{0}}".format(full_local_path))
        s3_file.get_contents_to_filename(full_local_path)
    except:
        print("Error downloading")


def deleteFile{sufix_methods}(bucket, s3_file):
        bucket.delete_key(s3_file)
        print("Deleted: {{0}}".format(s3_file.name))


class {class_name}{sufix_class}:

    def __init__(self, aws_key, aws_secret, use_ssl):
        self._aws_connection = S3Connection(aws_key, aws_secret, is_secure = use_ssl)

    def getFileNamesInBucket{sufix_methods}(self, aws_bucketname):
        if not self._bucketExists{sufix_methods}(aws_bucketname):
            self._printBucketNotFoundMessage{sufix_methods}(aws_bucketname)
            return list()
        else:
            bucket = self._aws_connection.get_bucket(aws_bucketname)
            return map(lambda aws_file_key: aws_file_key.name, bucket.list())

    def downloadFileFromBucket{sufix_methods}(self, aws_bucketname, filename, local_download_directory):
        if not self._bucketExists{sufix_methods}(aws_bucketname):
            self._printBucketNotFoundMessage{sufix_methods}(aws_bucketname)
        else:
            bucket = self._aws_connection.get_bucket(aws_bucketname)
            for s3_file in bucket.list():
                if filename == s3_file.name:
                    downloadFile{sufix_methods}(s3_file, local_download_directory)
                    break;

    def downloadAllFilesFromBucket{sufix_methods}(self, aws_bucketname, local_download_directory):
        if not self._bucketExists{sufix_methods}(aws_bucketname):
            self._printBucketNotFoundMessage{sufix_methods}(aws_bucketname)
        else:
            bucket = self._aws_connection.get_bucket(aws_bucketname)
            for s3_file in bucket.list():
                downloadFile{sufix_methods}(s3_file, local_download_directory)

    def deleteAllFilesFromBucket{sufix_methods}(self, aws_bucketname):
        if not self._bucketExists{sufix_methods}(aws_bucketname):
            self._printBucketNotFoundMessage{sufix_methods}(aws_bucketname)
        else:
            bucket = self._aws_connection.get_bucket{sufix_methods}(aws_bucketname)
            for s3_file in bucket.list():
                deleteFile{sufix_methods}(bucket, s3_file)

    def downloadFilesInBucketWithPredicate{sufix_methods}(self, aws_bucketname, filename_predicate, local_download_destination):
        if not self._bucketExists{sufix_methods}(aws_bucketname):
            self._printBucketNotFoundMessage{sufix_methods}(aws_bucketname)
        else:
            bucket = self._aws_connection.get_bucket(aws_bucketname)
            for s3_file in filter(lambda fkey: filename_predicate(fkey.name), bucket.list()):
                downloadFile{sufix_methods}(s3_file, local_download_destination)

    def deleteFilesInBucketWithPredicate{sufix_methods}(self, aws_bucketname, filename_predicate):
        if not self._bucketExists{sufix_methods}(aws_bucketname):
            self._printBucketNotFoundMessage{sufix_methods}(aws_bucketname)
        else:
            bucket = self._aws_connection.get_bucket(aws_bucketname)
            for s3_file in filter(lambda fkey: filename_predicate(fkey.name), bucket.list()):
                deleteFile{sufix_methods}(bucket, s3_file)

    def _bucketExists{sufix_methods}(self, bucket_name):
        return self._aws_connection.lookup(bucket_name) != None

    def _printBucketNotFoundMessage{sufix_methods}(self, bucket_name):
        print("Error: bucket '{{0}}' not found".format(bucket_name))

    """
    # print(str_code)
    if full_file_name:
        file_ptr = open(full_file_name, 'w+')
        file_ptr.write(str_code) 
        file_ptr.close()

def create_init_file(path):
    full_filename = os.path.join(path, "__init__.py")
    if not os.path.isfile(full_filename):
        with open(full_filename, "w+") as f_ptr:
            f_ptr.write("# This is a init file")


def create_folder(path=None, folder=None, subfolder=None, subsubfolder=None):
    if not path:
        print("Please provide a folder with absolute path")
        return
    if folder:
        current_path = os.path.join(path, folder)
        if os.path.isdir(current_path):
            if subfolder:
                current_path = os.path.join(current_path, subfolder)
                if os.path.isdir(current_path):
                    if subsubfolder:
                        current_path = os.path.join(current_path, subsubfolder)
                        if not os.path.isdir(current_path):
                            os.mkdir(current_path)
                        create_init_file(current_path)
                else:
                    os.mkdir(current_path)
                create_init_file(current_path)
        else:
            os.mkdir(current_path)
        create_init_file(current_path)

def get_caller_file_path():
    # Get the call stack as a list of tuples (frame object, filename, line number, function name, context line)
    call_stack = inspect.stack()
    # Get the caller's frame (index 1 in the call stack)
    caller_frame = call_stack[1]
    # Extract the caller's file path from the frame
    caller_file_path = os.path.abspath(caller_frame[1])
    caller_path = caller_file_path.replace(os.path.basename(caller_file_path), "")
    return caller_path

def create_package_sample(number_levels=2, number_replicas=10):
    """Creates a sample package with the following structure:
    
    """
    N_modules = number_replicas*number_levels
    N_submodules = number_replicas
    path = get_caller_file_path()
    path = os.path.join(path, "tests")
    package_name = "package_01"
    modules = ["module_"+str(i).zfill(2) for i in range(1, N_modules+1)]
    submodules = ["submodule_"+str(i).zfill(3) for i in range(1, N_submodules+1)]
    for i, module in enumerate(modules):
        for j, submodule in enumerate(submodules):
            create_folder(path=path, folder=package_name, subfolder=module, subsubfolder=submodule)
            full_file_name = path
            full_file_name = os.path.join(full_file_name, package_name)
            full_file_name = os.path.join(full_file_name, "module_"+str(i+1).zfill(2))
            full_file_name = os.path.join(full_file_name, "submodule_"+str(j+1).zfill(3))
            file_name = "file_"+str(i+1).zfill(2)+"_"+str(j+1).zfill(3)+".py"
            full_file_name = os.path.join(full_file_name, file_name)
            print(full_file_name)
            if i < 10:
                create_test_file(full_file_name=full_file_name, class_name="S3FileManager", sufix_class=str(i+1).zfill(2), sufix_methods=str(j+1).zfill(3))
            # TODO create logic to create nested imports, module 10*current_level+j imports number_replicas*(current_level-1)+j

    



# Function to search for library usage in a Python file
def find_library_usage(file_path):
    library_to_find = "requests"
    library_usages = []
    libraries_detected = set()
    modules_detected = set()
    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            tree = ast.parse(file.read())
        except SyntaxError:
            return library_usages
    counter_nodes = 0
    for node in ast.walk(tree):
        counter_nodes += 1
        if isinstance(node, ast.Import):
            for name in node.names:
                libraries_detected.add(name.name)
                if name.name == library_to_find:
                    library_usages.append((file_path, name.lineno))
        elif isinstance(node, ast.ImportFrom):
            modules_detected.add(node.module)
            if node.module == library_to_find:
                library_usages.append((file_path, node.lineno))
    print("counter_nodes:", counter_nodes)
    print("libraries_detected:",libraries_detected)
    print("modules_detected:",modules_detected)
    return library_usages

# Function to search for library usage in a directory
def search_directory(directory_path):
    library_usages = []
    
    for root, folders, files in os.walk(directory_path):
        # print("root:",root)
        # print("something:",folders)
        # print("files:",files)
        for file_name in files:
            if file_name.endswith('.py'):
                file_path = os.path.join(root, file_name)
                print(file_path)
                usages = find_library_usage(file_path)
                print(usages)
        #         library_usages.extend(usages)
    
    return library_usages


def test(search_directory_path="./"):
    print("Starting parser library")
    # Define the library/module you want to search for
    library_to_find = "requests"
    # Define the directory where you want to search for library usage

    if os.path.exists(search_directory_path):
        print("Exploring path: {0}".format(search_directory_path))
        library_usages = search_directory(search_directory_path)
        if library_usages:
            print(f'Library "{library_to_find}" is used in the following places:')
            for file_path, line_number in library_usages:
                print(f'File: {file_path}, Line: {line_number}')
        else:
            print(f'Library "{library_to_find}" is not used in the code.')
    else:
        print(f'Directory "{search_directory_path}" does not exist.')



def count_library_imports(file_path, library_name):
    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            tree = ast.parse(file.read())
        except SyntaxError:
            return 0  # Skip files with syntax errors

    import_count = 0

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for name in node.names:
                if name.name == library_name:
                    import_count += 1
        elif isinstance(node, ast.ImportFrom):
            if node.module == library_name:
                import_count += 1
    
    return import_count

if __name__=='__main__':
    # test()
    create_package_sample()
    # create_test_file(path="", class_name="S3FileMaganager_01", sufix_methods="_01")