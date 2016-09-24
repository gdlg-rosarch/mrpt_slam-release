Name:           ros-kinetic-mrpt-slam
Version:        0.1.2
Release:        0%{?dist}
Summary:        ROS mrpt_slam package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/mrpt_slam
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-kinetic-mrpt-ekf-slam-2d
Requires:       ros-kinetic-mrpt-ekf-slam-3d
Requires:       ros-kinetic-mrpt-icp-slam-2d
Requires:       ros-kinetic-mrpt-rbpf-slam
BuildRequires:  ros-kinetic-catkin

%description
mrpt_slam

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Sat Sep 24 2016 Vladislav Tananaev <v.d.tananaev@gmail.com> - 0.1.2-0
- Autogenerated by Bloom

* Mon Aug 22 2016 Vladislav Tananaev <v.d.tananaev@gmail.com> - 0.1.1-0
- Autogenerated by Bloom

