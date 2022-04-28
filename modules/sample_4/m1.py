from m2 import output1, output2, output3 #1 way

from package import file1 #2 way
from package.subpackage import file1 as f1 #(you can use (as name)alias to avoid confusion)

from package.file2 import package_2_file #3 way

output1()
output2()
output3()


f1.package_1_file()
#package_2_file()
file1.package_1_file()