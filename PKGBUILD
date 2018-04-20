# Script generated with Bloom
pkgdesc="ROS - This package is used for gridmap SLAM. The interface is similar to gmapping (http://wiki.ros.org/gmapping) but the package supports different particle-filter algorithms, range-only SLAM, can work with several grid maps simultaneously and more."
url='http://www.mrpt.org/'

pkgname='ros-kinetic-mrpt-rbpf-slam'
pkgver='0.1.5_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('mrpt'
'ros-kinetic-catkin'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-mrpt-bridge'
'ros-kinetic-nav-msgs'
'ros-kinetic-roscpp'
'ros-kinetic-roslib'
'ros-kinetic-rospy'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-tf'
'ros-kinetic-visualization-msgs'
)

depends=('mrpt'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-mrpt-bridge'
'ros-kinetic-nav-msgs'
'ros-kinetic-roscpp'
'ros-kinetic-roslib'
'ros-kinetic-rospy'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-tf'
)

conflicts=()
replaces=()

_dir=mrpt_rbpf_slam
source=()
md5sums=()

prepare() {
    cp -R $startdir/mrpt_rbpf_slam $srcdir/mrpt_rbpf_slam
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

