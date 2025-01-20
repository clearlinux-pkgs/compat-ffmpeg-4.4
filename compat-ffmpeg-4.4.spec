#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
# Source0 file verified with key 0xB4322F04D67658D8 (ffmpeg-devel@ffmpeg.org)
#
Name     : compat-ffmpeg-4.4
Version  : 4.4.4
Release  : 9
URL      : https://ffmpeg.org/releases/ffmpeg-4.4.4.tar.xz
Source0  : https://ffmpeg.org/releases/ffmpeg-4.4.4.tar.xz
Source1  : https://ffmpeg.org/releases/ffmpeg-4.4.4.tar.xz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 LGPL-2.1 LGPL-3.0
Requires: compat-ffmpeg-4.4-lib = %{version}-%{release}
Requires: compat-ffmpeg-4.4-license = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : gmp-dev
BuildRequires : ladspa_sdk-dev
BuildRequires : libass-dev
BuildRequires : libtheora-dev
BuildRequires : nasm
BuildRequires : pkgconfig(aom)
BuildRequires : pkgconfig(dav1d)
BuildRequires : pkgconfig(jack)
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libmfx)
BuildRequires : pkgconfig(libopenjp2)
BuildRequires : pkgconfig(libopenmpt)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(librsvg-2.0)
BuildRequires : pkgconfig(libssh)
BuildRequires : pkgconfig(libv4l2)
BuildRequires : pkgconfig(libva)
BuildRequires : pkgconfig(libwebp)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(opus)
BuildRequires : pkgconfig(sdl2)
BuildRequires : pkgconfig(speex)
BuildRequires : pkgconfig(srt)
BuildRequires : pkgconfig(vidstab)
BuildRequires : pkgconfig(vorbis)
BuildRequires : pkgconfig(vpx)
BuildRequires : pkgconfig(x264)
BuildRequires : pkgconfig(x265)
BuildRequires : pkgconfig(zimg)
BuildRequires : rtmpdump-dev
BuildRequires : xvidcore-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-configure-do-not-die-if-unknown-option-is-found.patch

%description
----------------------
Both following use cases rely on pkg-config and make, thus make sure
that you have them installed and working on your system.

%package lib
Summary: lib components for the compat-ffmpeg-4.4 package.
Group: Libraries
Requires: compat-ffmpeg-4.4-license = %{version}-%{release}

%description lib
lib components for the compat-ffmpeg-4.4 package.


%package license
Summary: license components for the compat-ffmpeg-4.4 package.
Group: Default

%description license
license components for the compat-ffmpeg-4.4 package.


%prep
%setup -q -n ffmpeg-4.4.4
cd %{_builddir}/ffmpeg-4.4.4
%patch -P 1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1693417532
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%configure --disable-static --disable-debug \
--disable-static \
--disable-stripping \
--enable-lto \
--enable-fontconfig \
--enable-gmp \
--enable-gnutls \
--enable-gpl \
--enable-ladspa \
--enable-libaom \
--enable-libass \
--enable-libdav1d \
--enable-libdrm \
--enable-libfreetype \
--enable-libfribidi \
--enable-libjack \
--enable-libmfx \
--enable-libopenjpeg \
--enable-libopenmpt \
--enable-libopus \
--enable-libpulse \
--enable-librsvg \
--enable-libspeex \
--enable-libsrt \
--enable-libssh \
--enable-libtheora \
--enable-libv4l2 \
--enable-libvidstab \
--enable-libvorbis \
--enable-libvpx \
--enable-libwebp \
--enable-libx264 \
--enable-libx265 \
--enable-libxcb \
--enable-libxml2 \
--enable-libxvid \
--enable-libzimg \
--enable-shared \
--enable-version3 \
--disable-asm
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1693417532
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/compat-ffmpeg-4.4
cp %{_builddir}/ffmpeg-%{version}/COPYING.GPLv2 %{buildroot}/usr/share/package-licenses/compat-ffmpeg-4.4/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/ffmpeg-%{version}/COPYING.GPLv3 %{buildroot}/usr/share/package-licenses/compat-ffmpeg-4.4/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/ffmpeg-%{version}/COPYING.LGPLv2.1 %{buildroot}/usr/share/package-licenses/compat-ffmpeg-4.4/37d2f1d62fec4da0caf06e5da21afc3521b597aa || :
cp %{_builddir}/ffmpeg-%{version}/COPYING.LGPLv3 %{buildroot}/usr/share/package-licenses/compat-ffmpeg-4.4/f45ee1c765646813b442ca58de72e20a64a7ddba || :
%make_install
## Remove excluded files
rm -f %{buildroot}*/usr/bin/ffmpeg
rm -f %{buildroot}*/usr/bin/ffplay
rm -f %{buildroot}*/usr/bin/ffprobe
rm -f %{buildroot}*/usr/include/libavcodec/ac3_parser.h
rm -f %{buildroot}*/usr/include/libavcodec/adts_parser.h
rm -f %{buildroot}*/usr/include/libavcodec/avcodec.h
rm -f %{buildroot}*/usr/include/libavcodec/avdct.h
rm -f %{buildroot}*/usr/include/libavcodec/avfft.h
rm -f %{buildroot}*/usr/include/libavcodec/bsf.h
rm -f %{buildroot}*/usr/include/libavcodec/codec.h
rm -f %{buildroot}*/usr/include/libavcodec/codec_desc.h
rm -f %{buildroot}*/usr/include/libavcodec/codec_id.h
rm -f %{buildroot}*/usr/include/libavcodec/codec_par.h
rm -f %{buildroot}*/usr/include/libavcodec/d3d11va.h
rm -f %{buildroot}*/usr/include/libavcodec/dirac.h
rm -f %{buildroot}*/usr/include/libavcodec/dv_profile.h
rm -f %{buildroot}*/usr/include/libavcodec/dxva2.h
rm -f %{buildroot}*/usr/include/libavcodec/jni.h
rm -f %{buildroot}*/usr/include/libavcodec/mediacodec.h
rm -f %{buildroot}*/usr/include/libavcodec/packet.h
rm -f %{buildroot}*/usr/include/libavcodec/qsv.h
rm -f %{buildroot}*/usr/include/libavcodec/vaapi.h
rm -f %{buildroot}*/usr/include/libavcodec/vdpau.h
rm -f %{buildroot}*/usr/include/libavcodec/version.h
rm -f %{buildroot}*/usr/include/libavcodec/videotoolbox.h
rm -f %{buildroot}*/usr/include/libavcodec/vorbis_parser.h
rm -f %{buildroot}*/usr/include/libavcodec/xvmc.h
rm -f %{buildroot}*/usr/include/libavdevice/avdevice.h
rm -f %{buildroot}*/usr/include/libavdevice/version.h
rm -f %{buildroot}*/usr/include/libavfilter/avfilter.h
rm -f %{buildroot}*/usr/include/libavfilter/buffersink.h
rm -f %{buildroot}*/usr/include/libavfilter/buffersrc.h
rm -f %{buildroot}*/usr/include/libavfilter/version.h
rm -f %{buildroot}*/usr/include/libavformat/avformat.h
rm -f %{buildroot}*/usr/include/libavformat/avio.h
rm -f %{buildroot}*/usr/include/libavformat/version.h
rm -f %{buildroot}*/usr/include/libavutil/adler32.h
rm -f %{buildroot}*/usr/include/libavutil/aes.h
rm -f %{buildroot}*/usr/include/libavutil/aes_ctr.h
rm -f %{buildroot}*/usr/include/libavutil/attributes.h
rm -f %{buildroot}*/usr/include/libavutil/audio_fifo.h
rm -f %{buildroot}*/usr/include/libavutil/avassert.h
rm -f %{buildroot}*/usr/include/libavutil/avconfig.h
rm -f %{buildroot}*/usr/include/libavutil/avstring.h
rm -f %{buildroot}*/usr/include/libavutil/avutil.h
rm -f %{buildroot}*/usr/include/libavutil/base64.h
rm -f %{buildroot}*/usr/include/libavutil/blowfish.h
rm -f %{buildroot}*/usr/include/libavutil/bprint.h
rm -f %{buildroot}*/usr/include/libavutil/bswap.h
rm -f %{buildroot}*/usr/include/libavutil/buffer.h
rm -f %{buildroot}*/usr/include/libavutil/camellia.h
rm -f %{buildroot}*/usr/include/libavutil/cast5.h
rm -f %{buildroot}*/usr/include/libavutil/channel_layout.h
rm -f %{buildroot}*/usr/include/libavutil/common.h
rm -f %{buildroot}*/usr/include/libavutil/cpu.h
rm -f %{buildroot}*/usr/include/libavutil/crc.h
rm -f %{buildroot}*/usr/include/libavutil/des.h
rm -f %{buildroot}*/usr/include/libavutil/dict.h
rm -f %{buildroot}*/usr/include/libavutil/display.h
rm -f %{buildroot}*/usr/include/libavutil/dovi_meta.h
rm -f %{buildroot}*/usr/include/libavutil/downmix_info.h
rm -f %{buildroot}*/usr/include/libavutil/encryption_info.h
rm -f %{buildroot}*/usr/include/libavutil/error.h
rm -f %{buildroot}*/usr/include/libavutil/eval.h
rm -f %{buildroot}*/usr/include/libavutil/ffversion.h
rm -f %{buildroot}*/usr/include/libavutil/fifo.h
rm -f %{buildroot}*/usr/include/libavutil/file.h
rm -f %{buildroot}*/usr/include/libavutil/film_grain_params.h
rm -f %{buildroot}*/usr/include/libavutil/frame.h
rm -f %{buildroot}*/usr/include/libavutil/hash.h
rm -f %{buildroot}*/usr/include/libavutil/hdr_dynamic_metadata.h
rm -f %{buildroot}*/usr/include/libavutil/hmac.h
rm -f %{buildroot}*/usr/include/libavutil/hwcontext.h
rm -f %{buildroot}*/usr/include/libavutil/hwcontext_cuda.h
rm -f %{buildroot}*/usr/include/libavutil/hwcontext_d3d11va.h
rm -f %{buildroot}*/usr/include/libavutil/hwcontext_drm.h
rm -f %{buildroot}*/usr/include/libavutil/hwcontext_dxva2.h
rm -f %{buildroot}*/usr/include/libavutil/hwcontext_mediacodec.h
rm -f %{buildroot}*/usr/include/libavutil/hwcontext_opencl.h
rm -f %{buildroot}*/usr/include/libavutil/hwcontext_qsv.h
rm -f %{buildroot}*/usr/include/libavutil/hwcontext_vaapi.h
rm -f %{buildroot}*/usr/include/libavutil/hwcontext_vdpau.h
rm -f %{buildroot}*/usr/include/libavutil/hwcontext_videotoolbox.h
rm -f %{buildroot}*/usr/include/libavutil/hwcontext_vulkan.h
rm -f %{buildroot}*/usr/include/libavutil/imgutils.h
rm -f %{buildroot}*/usr/include/libavutil/intfloat.h
rm -f %{buildroot}*/usr/include/libavutil/intreadwrite.h
rm -f %{buildroot}*/usr/include/libavutil/lfg.h
rm -f %{buildroot}*/usr/include/libavutil/log.h
rm -f %{buildroot}*/usr/include/libavutil/lzo.h
rm -f %{buildroot}*/usr/include/libavutil/macros.h
rm -f %{buildroot}*/usr/include/libavutil/mastering_display_metadata.h
rm -f %{buildroot}*/usr/include/libavutil/mathematics.h
rm -f %{buildroot}*/usr/include/libavutil/md5.h
rm -f %{buildroot}*/usr/include/libavutil/mem.h
rm -f %{buildroot}*/usr/include/libavutil/motion_vector.h
rm -f %{buildroot}*/usr/include/libavutil/murmur3.h
rm -f %{buildroot}*/usr/include/libavutil/opt.h
rm -f %{buildroot}*/usr/include/libavutil/parseutils.h
rm -f %{buildroot}*/usr/include/libavutil/pixdesc.h
rm -f %{buildroot}*/usr/include/libavutil/pixelutils.h
rm -f %{buildroot}*/usr/include/libavutil/pixfmt.h
rm -f %{buildroot}*/usr/include/libavutil/random_seed.h
rm -f %{buildroot}*/usr/include/libavutil/rational.h
rm -f %{buildroot}*/usr/include/libavutil/rc4.h
rm -f %{buildroot}*/usr/include/libavutil/replaygain.h
rm -f %{buildroot}*/usr/include/libavutil/ripemd.h
rm -f %{buildroot}*/usr/include/libavutil/samplefmt.h
rm -f %{buildroot}*/usr/include/libavutil/sha.h
rm -f %{buildroot}*/usr/include/libavutil/sha512.h
rm -f %{buildroot}*/usr/include/libavutil/spherical.h
rm -f %{buildroot}*/usr/include/libavutil/stereo3d.h
rm -f %{buildroot}*/usr/include/libavutil/tea.h
rm -f %{buildroot}*/usr/include/libavutil/threadmessage.h
rm -f %{buildroot}*/usr/include/libavutil/time.h
rm -f %{buildroot}*/usr/include/libavutil/timecode.h
rm -f %{buildroot}*/usr/include/libavutil/timestamp.h
rm -f %{buildroot}*/usr/include/libavutil/tree.h
rm -f %{buildroot}*/usr/include/libavutil/twofish.h
rm -f %{buildroot}*/usr/include/libavutil/tx.h
rm -f %{buildroot}*/usr/include/libavutil/version.h
rm -f %{buildroot}*/usr/include/libavutil/video_enc_params.h
rm -f %{buildroot}*/usr/include/libavutil/xtea.h
rm -f %{buildroot}*/usr/include/libpostproc/postprocess.h
rm -f %{buildroot}*/usr/include/libpostproc/version.h
rm -f %{buildroot}*/usr/include/libswresample/swresample.h
rm -f %{buildroot}*/usr/include/libswresample/version.h
rm -f %{buildroot}*/usr/include/libswscale/swscale.h
rm -f %{buildroot}*/usr/include/libswscale/version.h
rm -f %{buildroot}*/usr/lib64/libavcodec.so
rm -f %{buildroot}*/usr/lib64/libavdevice.so
rm -f %{buildroot}*/usr/lib64/libavfilter.so
rm -f %{buildroot}*/usr/lib64/libavformat.so
rm -f %{buildroot}*/usr/lib64/libavutil.so
rm -f %{buildroot}*/usr/lib64/libpostproc.so
rm -f %{buildroot}*/usr/lib64/libswresample.so
rm -f %{buildroot}*/usr/lib64/libswscale.so
rm -f %{buildroot}*/usr/lib64/pkgconfig/libavcodec.pc
rm -f %{buildroot}*/usr/lib64/pkgconfig/libavdevice.pc
rm -f %{buildroot}*/usr/lib64/pkgconfig/libavfilter.pc
rm -f %{buildroot}*/usr/lib64/pkgconfig/libavformat.pc
rm -f %{buildroot}*/usr/lib64/pkgconfig/libavutil.pc
rm -f %{buildroot}*/usr/lib64/pkgconfig/libpostproc.pc
rm -f %{buildroot}*/usr/lib64/pkgconfig/libswresample.pc
rm -f %{buildroot}*/usr/lib64/pkgconfig/libswscale.pc
rm -f %{buildroot}*/usr/share/examples/Makefile
rm -f %{buildroot}*/usr/share/examples/README
rm -f %{buildroot}*/usr/share/examples/avio_list_dir.c
rm -f %{buildroot}*/usr/share/examples/avio_reading.c
rm -f %{buildroot}*/usr/share/examples/decode_audio.c
rm -f %{buildroot}*/usr/share/examples/decode_video.c
rm -f %{buildroot}*/usr/share/examples/demuxing_decoding.c
rm -f %{buildroot}*/usr/share/examples/encode_audio.c
rm -f %{buildroot}*/usr/share/examples/encode_video.c
rm -f %{buildroot}*/usr/share/examples/extract_mvs.c
rm -f %{buildroot}*/usr/share/examples/filter_audio.c
rm -f %{buildroot}*/usr/share/examples/filtering_audio.c
rm -f %{buildroot}*/usr/share/examples/filtering_video.c
rm -f %{buildroot}*/usr/share/examples/http_multiclient.c
rm -f %{buildroot}*/usr/share/examples/hw_decode.c
rm -f %{buildroot}*/usr/share/examples/metadata.c
rm -f %{buildroot}*/usr/share/examples/muxing.c
rm -f %{buildroot}*/usr/share/examples/qsvdec.c
rm -f %{buildroot}*/usr/share/examples/remuxing.c
rm -f %{buildroot}*/usr/share/examples/resampling_audio.c
rm -f %{buildroot}*/usr/share/examples/scaling_video.c
rm -f %{buildroot}*/usr/share/examples/transcode_aac.c
rm -f %{buildroot}*/usr/share/examples/transcoding.c
rm -f %{buildroot}*/usr/share/examples/vaapi_encode.c
rm -f %{buildroot}*/usr/share/examples/vaapi_transcode.c
rm -f %{buildroot}*/usr/share/ffprobe.xsd
rm -f %{buildroot}*/usr/share/libvpx-1080p.ffpreset
rm -f %{buildroot}*/usr/share/libvpx-1080p50_60.ffpreset
rm -f %{buildroot}*/usr/share/libvpx-360p.ffpreset
rm -f %{buildroot}*/usr/share/libvpx-720p.ffpreset
rm -f %{buildroot}*/usr/share/libvpx-720p50_60.ffpreset
rm -f %{buildroot}*/usr/share/man/man1/ffmpeg-all.1
rm -f %{buildroot}*/usr/share/man/man1/ffmpeg-bitstream-filters.1
rm -f %{buildroot}*/usr/share/man/man1/ffmpeg-codecs.1
rm -f %{buildroot}*/usr/share/man/man1/ffmpeg-devices.1
rm -f %{buildroot}*/usr/share/man/man1/ffmpeg-filters.1
rm -f %{buildroot}*/usr/share/man/man1/ffmpeg-formats.1
rm -f %{buildroot}*/usr/share/man/man1/ffmpeg-protocols.1
rm -f %{buildroot}*/usr/share/man/man1/ffmpeg-resampler.1
rm -f %{buildroot}*/usr/share/man/man1/ffmpeg-scaler.1
rm -f %{buildroot}*/usr/share/man/man1/ffmpeg-utils.1
rm -f %{buildroot}*/usr/share/man/man1/ffmpeg.1
rm -f %{buildroot}*/usr/share/man/man1/ffplay-all.1
rm -f %{buildroot}*/usr/share/man/man1/ffplay.1
rm -f %{buildroot}*/usr/share/man/man1/ffprobe-all.1
rm -f %{buildroot}*/usr/share/man/man1/ffprobe.1
rm -f %{buildroot}*/usr/share/man/man3/libavcodec.3
rm -f %{buildroot}*/usr/share/man/man3/libavdevice.3
rm -f %{buildroot}*/usr/share/man/man3/libavfilter.3
rm -f %{buildroot}*/usr/share/man/man3/libavformat.3
rm -f %{buildroot}*/usr/share/man/man3/libavutil.3
rm -f %{buildroot}*/usr/share/man/man3/libswresample.3
rm -f %{buildroot}*/usr/share/man/man3/libswscale.3

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/libavcodec.so.58
/usr/lib64/libavcodec.so.58.134.100
/usr/lib64/libavdevice.so.58
/usr/lib64/libavdevice.so.58.13.100
/usr/lib64/libavfilter.so.7
/usr/lib64/libavfilter.so.7.110.100
/usr/lib64/libavformat.so.58
/usr/lib64/libavformat.so.58.76.100
/usr/lib64/libavutil.so.56
/usr/lib64/libavutil.so.56.70.100
/usr/lib64/libpostproc.so.55
/usr/lib64/libpostproc.so.55.9.100
/usr/lib64/libswresample.so.3
/usr/lib64/libswresample.so.3.9.100
/usr/lib64/libswscale.so.5
/usr/lib64/libswscale.so.5.9.100

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/compat-ffmpeg-4.4/37d2f1d62fec4da0caf06e5da21afc3521b597aa
/usr/share/package-licenses/compat-ffmpeg-4.4/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/compat-ffmpeg-4.4/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/compat-ffmpeg-4.4/f45ee1c765646813b442ca58de72e20a64a7ddba
