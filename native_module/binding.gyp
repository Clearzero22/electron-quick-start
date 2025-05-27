{
  "targets": [
    {
      "target_name": "my_module",
      "sources": [ "my_module.cc" ],
      "cflags!": [ "-fno-exceptions" ],
      "cflags_cc!": [ "-fno-exceptions" ],
      "defines": [ 'NAPI_VERSION=8' ],
      "include_dirs": [
         "<!@(node -p \"require('node-addon-api').include\")"
      ] ,
            'defines': [ 'NAPI_DISABLE_CPP_EXCEPTIONS' ],
    }
  ]
}