# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: svga.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nsvga.proto\x12\x13\x63om.opensource.svga\"W\n\x0bMovieParams\x12\x14\n\x0cviewBoxWidth\x18\x01 \x01(\x02\x12\x15\n\rviewBoxHeight\x18\x02 \x01(\x02\x12\x0b\n\x03\x66ps\x18\x03 \x01(\x05\x12\x0e\n\x06\x66rames\x18\x04 \x01(\x05\"d\n\x0cSpriteEntity\x12\x10\n\x08imageKey\x18\x01 \x01(\t\x12\x30\n\x06\x66rames\x18\x02 \x03(\x0b\x32 .com.opensource.svga.FrameEntity\x12\x10\n\x08matteKey\x18\x03 \x01(\t\"k\n\x0b\x41udioEntity\x12\x10\n\x08\x61udioKey\x18\x01 \x01(\t\x12\x12\n\nstartFrame\x18\x02 \x01(\x05\x12\x10\n\x08\x65ndFrame\x18\x03 \x01(\x05\x12\x11\n\tstartTime\x18\x04 \x01(\x05\x12\x11\n\ttotalTime\x18\x05 \x01(\x05\"=\n\x06Layout\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\r\n\x05width\x18\x03 \x01(\x02\x12\x0e\n\x06height\x18\x04 \x01(\x02\"O\n\tTransform\x12\t\n\x01\x61\x18\x01 \x01(\x02\x12\t\n\x01\x62\x18\x02 \x01(\x02\x12\t\n\x01\x63\x18\x03 \x01(\x02\x12\t\n\x01\x64\x18\x04 \x01(\x02\x12\n\n\x02tx\x18\x05 \x01(\x02\x12\n\n\x02ty\x18\x06 \x01(\x02\"\xba\t\n\x0bShapeEntity\x12\x38\n\x04type\x18\x01 \x01(\x0e\x32*.com.opensource.svga.ShapeEntity.ShapeType\x12;\n\x05shape\x18\x02 \x01(\x0b\x32*.com.opensource.svga.ShapeEntity.ShapeArgsH\x00\x12\x39\n\x04rect\x18\x03 \x01(\x0b\x32).com.opensource.svga.ShapeEntity.RectArgsH\x00\x12?\n\x07\x65llipse\x18\x04 \x01(\x0b\x32,.com.opensource.svga.ShapeEntity.EllipseArgsH\x00\x12;\n\x06styles\x18\n \x01(\x0b\x32+.com.opensource.svga.ShapeEntity.ShapeStyle\x12\x31\n\ttransform\x18\x0b \x01(\x0b\x32\x1e.com.opensource.svga.Transform\x1a\x16\n\tShapeArgs\x12\t\n\x01\x64\x18\x01 \x01(\t\x1aU\n\x08RectArgs\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\r\n\x05width\x18\x03 \x01(\x02\x12\x0e\n\x06height\x18\x04 \x01(\x02\x12\x14\n\x0c\x63ornerRadius\x18\x05 \x01(\x02\x1a\x45\n\x0b\x45llipseArgs\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\x0f\n\x07radiusX\x18\x03 \x01(\x02\x12\x0f\n\x07radiusY\x18\x04 \x01(\x02\x1a\xd0\x04\n\nShapeStyle\x12\x43\n\x04\x66ill\x18\x01 \x01(\x0b\x32\x35.com.opensource.svga.ShapeEntity.ShapeStyle.RGBAColor\x12\x45\n\x06stroke\x18\x02 \x01(\x0b\x32\x35.com.opensource.svga.ShapeEntity.ShapeStyle.RGBAColor\x12\x13\n\x0bstrokeWidth\x18\x03 \x01(\x02\x12\x44\n\x07lineCap\x18\x04 \x01(\x0e\x32\x33.com.opensource.svga.ShapeEntity.ShapeStyle.LineCap\x12\x46\n\x08lineJoin\x18\x05 \x01(\x0e\x32\x34.com.opensource.svga.ShapeEntity.ShapeStyle.LineJoin\x12\x12\n\nmiterLimit\x18\x06 \x01(\x02\x12\x11\n\tlineDashI\x18\x07 \x01(\x02\x12\x12\n\nlineDashII\x18\x08 \x01(\x02\x12\x13\n\x0blineDashIII\x18\t \x01(\x02\x1a\x37\n\tRGBAColor\x12\t\n\x01r\x18\x01 \x01(\x02\x12\t\n\x01g\x18\x02 \x01(\x02\x12\t\n\x01\x62\x18\x03 \x01(\x02\x12\t\n\x01\x61\x18\x04 \x01(\x02\"B\n\x07LineCap\x12\x10\n\x0cLineCap_BUTT\x10\x00\x12\x11\n\rLineCap_ROUND\x10\x01\x12\x12\n\x0eLineCap_SQUARE\x10\x02\"F\n\x08LineJoin\x12\x12\n\x0eLineJoin_MITER\x10\x00\x12\x12\n\x0eLineJoin_ROUND\x10\x01\x12\x12\n\x0eLineJoin_BEVEL\x10\x02\"7\n\tShapeType\x12\t\n\x05SHAPE\x10\x00\x12\x08\n\x04RECT\x10\x01\x12\x0b\n\x07\x45LLIPSE\x10\x02\x12\x08\n\x04KEEP\x10\x03\x42\x06\n\x04\x61rgs\"\xc0\x01\n\x0b\x46rameEntity\x12\r\n\x05\x61lpha\x18\x01 \x01(\x02\x12+\n\x06layout\x18\x02 \x01(\x0b\x32\x1b.com.opensource.svga.Layout\x12\x31\n\ttransform\x18\x03 \x01(\x0b\x32\x1e.com.opensource.svga.Transform\x12\x10\n\x08\x63lipPath\x18\x04 \x01(\t\x12\x30\n\x06shapes\x18\x05 \x03(\x0b\x32 .com.opensource.svga.ShapeEntity\"\xa3\x02\n\x0bMovieEntity\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x30\n\x06params\x18\x02 \x01(\x0b\x32 .com.opensource.svga.MovieParams\x12<\n\x06images\x18\x03 \x03(\x0b\x32,.com.opensource.svga.MovieEntity.ImagesEntry\x12\x32\n\x07sprites\x18\x04 \x03(\x0b\x32!.com.opensource.svga.SpriteEntity\x12\x30\n\x06\x61udios\x18\x05 \x03(\x0b\x32 .com.opensource.svga.AudioEntity\x1a-\n\x0bImagesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\x42-\n\x1f\x63om.opensource.svgaplayer.proto\xa2\x02\tSVGAProtob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'svga_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\037com.opensource.svgaplayer.proto\242\002\tSVGAProto'
  _MOVIEENTITY_IMAGESENTRY._options = None
  _MOVIEENTITY_IMAGESENTRY._serialized_options = b'8\001'
  _MOVIEPARAMS._serialized_start=35
  _MOVIEPARAMS._serialized_end=122
  _SPRITEENTITY._serialized_start=124
  _SPRITEENTITY._serialized_end=224
  _AUDIOENTITY._serialized_start=226
  _AUDIOENTITY._serialized_end=333
  _LAYOUT._serialized_start=335
  _LAYOUT._serialized_end=396
  _TRANSFORM._serialized_start=398
  _TRANSFORM._serialized_end=477
  _SHAPEENTITY._serialized_start=480
  _SHAPEENTITY._serialized_end=1690
  _SHAPEENTITY_SHAPEARGS._serialized_start=850
  _SHAPEENTITY_SHAPEARGS._serialized_end=872
  _SHAPEENTITY_RECTARGS._serialized_start=874
  _SHAPEENTITY_RECTARGS._serialized_end=959
  _SHAPEENTITY_ELLIPSEARGS._serialized_start=961
  _SHAPEENTITY_ELLIPSEARGS._serialized_end=1030
  _SHAPEENTITY_SHAPESTYLE._serialized_start=1033
  _SHAPEENTITY_SHAPESTYLE._serialized_end=1625
  _SHAPEENTITY_SHAPESTYLE_RGBACOLOR._serialized_start=1430
  _SHAPEENTITY_SHAPESTYLE_RGBACOLOR._serialized_end=1485
  _SHAPEENTITY_SHAPESTYLE_LINECAP._serialized_start=1487
  _SHAPEENTITY_SHAPESTYLE_LINECAP._serialized_end=1553
  _SHAPEENTITY_SHAPESTYLE_LINEJOIN._serialized_start=1555
  _SHAPEENTITY_SHAPESTYLE_LINEJOIN._serialized_end=1625
  _SHAPEENTITY_SHAPETYPE._serialized_start=1627
  _SHAPEENTITY_SHAPETYPE._serialized_end=1682
  _FRAMEENTITY._serialized_start=1693
  _FRAMEENTITY._serialized_end=1885
  _MOVIEENTITY._serialized_start=1888
  _MOVIEENTITY._serialized_end=2179
  _MOVIEENTITY_IMAGESENTRY._serialized_start=2134
  _MOVIEENTITY_IMAGESENTRY._serialized_end=2179
# @@protoc_insertion_point(module_scope)
