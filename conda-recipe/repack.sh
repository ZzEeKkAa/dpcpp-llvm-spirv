#!/bin/bash
echo -e "Start building dpcpp-llvm-spirv package \n"
src="${SRC_DIR}"

echo "Python: ${PYTHON}"
[ -z "${PYTHON}" ] && exit 1

pushd $src/package
${PYTHON} setup.py install --single-version-externally-managed --record=llvm_spirv_record.txt
cat llvm_spirv_record.txt
popd

echo -e "Done building the Python package. Start vendoring of llvm-spirv executable \n"

pushd ${src}/compiler
cp bin-llvm/llvm-spirv $(${PYTHON} -c "import dpcpp_llvm_spirv as p; print(p.get_llvm_spirv_path())")
echo "copy llvm-spirv to: $(${PYTHON} -c "import dpcpp_llvm_spirv as p; print(p.get_llvm_spirv_path())")"
popd
echo "done. \n"
