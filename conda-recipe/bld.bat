
pushd %SRC_DIR%\package
%PYTHON% setup.py install --single-version-externally-managed --record=llvm_spirv_record.txt
type llvm_spirv_record.txt
popd

pushd %SRC_DIR%\compiler
%PYTHON% -c "import dpcpp_llvm_spirv as p; print(p.get_llvm_spirv_path())" > Output
set /p DIRSTR= < Output
copy bin-llvm\llvm-spirv %DIRSTR%
del Output
popd
