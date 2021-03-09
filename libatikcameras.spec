Name:      libatikcameras
Version:   2020_10_19
Release:   0
Url:       https://www.atik-cameras.com/software-downloads/
Summary:   Custom packaging of Atik camera library from the official website.
License:   proprietary
Group:     Unspecified
BuildArch: x86_64
Source: AtikCamerasSDK_%{version}.zip

%description
Custom packaging of Atik camera library from the official website.

%prep
%setup -qcn AtikCamerasSDK_%{version}

%build

mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_udevrulesdir}
%{__install} AtikCamerasSDK_%{version}/lib/linux/64/NoFlyCapture/libatikcameras.so %{buildroot}%{_libdir}
%{__install} AtikCamerasSDK_%{version}/include/AtikCameras.h %{buildroot}%{_includedir}
%{__install} AtikCamerasSDK_%{version}/lib/linux/atik.rules %{buildroot}%{_udevrulesdir}/10-atikcameras.rules

%files
%defattr(0644,root,root,-)
%{_libdir}/libatikcameras.so
%{_includedir}/AtikCameras.h
%{_udevrulesdir}/10-atikcameras.rules

%changelog
