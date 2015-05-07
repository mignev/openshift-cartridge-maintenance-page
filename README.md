# OpenShift Maintenance Page

This cartridge is build for [http://www.startapp.bg](http://www.startapp.bg).

During the deployments when `hot_deploy` isn't enabled you see the default `503` page of the Apache Server.
This cartridge will replace this page with another one which is much more user friendly :)

# Usage exmaple

### Add Maintenance Page Cartridge

Example with StartApp.bg

```sh
  app cartridge add http://j.mp/maintenance_page -a <appname>
```

Example with standart OpenShift installation or Online

```sh
  rhc cartridge add http://j.mp/maintenance_page -a <appname>
```

### Costomization

You can change default maintenance page with some custom one.

Example with StartApp.bg

```sh
  app env set MAINTENANCE_URL=https://gist.githubusercontent.com/mignev/af92a493ed98b5d3815e/raw/8e5f7dbcd1f50eda507400aa6fd14530e2f9bdac/maintenance.html -a <myapp>
```

Example with standart OpenShift installation or Online

```sh
  rhc env set MAINTENANCE_URL=https://gist.githubusercontent.com/mignev/af92a493ed98b5d3815e/raw/8e5f7dbcd1f50eda507400aa6fd14530e2f9bdac/maintenance.html -a <myapp>
```

# Contributing

So thank you very much that you are looking in this section :) I will be very happy and thankful if you share some ideas, some hacks and best practices which will make our lives nicer and easier :)

Fork the [openshift-cartridge-maintenance-page repo on GitHub](https://github.com/mignev/openshift-cartridge-maintenance-page), make your super duper awesome changes :) and send me a Pull Request. :)


#Copyright
Copyright (c) 2014 Marian Ignev. See LICENSE for further details.
