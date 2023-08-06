FROM ciimage/python:3.9 as cairo-lang-builder

RUN apt update && apt install -y make libgmp3-dev g++ python3-pip python3.9-dev python3.9-venv npm cargo
# Installing cmake via apt doesn't bring the most up-to-date version.
RUN pip install --upgrade pip
RUN pip install cmake==3.22 maturin

# Install solc and ganache
RUN curl https://binaries.soliditylang.org/linux-amd64/solc-linux-amd64-v0.6.12+commit.27d51765 -o /usr/local/bin/solc-0.6.12
RUN echo 'f6cb519b01dabc61cab4c184a3db11aa591d18151e362fcae850e42cffdfb09a /usr/local/bin/solc-0.6.12' | sha256sum --check
RUN chmod +x /usr/local/bin/solc-0.6.12
RUN npm install -g --unsafe-perm ganache@7.4.3

COPY . /app

# Build.
WORKDIR /app
RUN CARGO_INCREMENTAL=0 maturin build --release --strip --interpreter 3.9
RUN pip install target/wheels/cairo_rs_py-0.1.0-cp39-cp39-manylinux_2_31_x86_64.whl

WORKDIR /app/cairo-lang
RUN ./build.sh

WORKDIR /app/cairo-lang
RUN make all -j8

# Run tests.
RUN ctest -V -j8

#WORKDIR /app/cairo-lang
RUN src/starkware/cairo/lang/package_test/run_test.sh
