# CHANGELOG - gunicorn

## 2.3.0 / 2022-04-05

* [Added] Add metric_patterns options to filter all metric submission by a list of regexes. See [#11695](https://github.com/DataDog/integrations-core/pull/11695).

## 2.2.0 / 2022-02-19

* [Added] Add `pyproject.toml` file. See [#11357](https://github.com/DataDog/integrations-core/pull/11357).
* [Added] Upgrade psutil to 5.9.0. See [#11139](https://github.com/DataDog/integrations-core/pull/11139).
* [Fixed] Fix namespace packaging on Python 2. See [#11532](https://github.com/DataDog/integrations-core/pull/11532).

## 2.1.1 / 2022-01-08 / Agent 7.34.0

* [Fixed] Add comment to autogenerated model files. See [#10945](https://github.com/DataDog/integrations-core/pull/10945).

## 2.1.0 / 2021-10-04 / Agent 7.32.0

* [Added] Disable generic tags. See [#10027](https://github.com/DataDog/integrations-core/pull/10027).

## 2.0.0 / 2021-08-22 / Agent 7.31.0

* [Changed] Remove messages for integrations for OK service checks. See [#9888](https://github.com/DataDog/integrations-core/pull/9888).

## 1.15.0 / 2021-05-28 / Agent 7.29.0

* [Added] Add runtime configuration validation. See [#8923](https://github.com/DataDog/integrations-core/pull/8923).

## 1.14.2 / 2021-03-07 / Agent 7.27.0

* [Fixed] Bump minimum base package version. See [#8443](https://github.com/DataDog/integrations-core/pull/8443).
* [Fixed] Improve readability a bit. See [#8454](https://github.com/DataDog/integrations-core/pull/8454).

## 1.14.1 / 2021-01-15 / Agent 7.26.0

* [Fixed] Prevent raising an error if the master process no longer exists. See [#8314](https://github.com/DataDog/integrations-core/pull/8314).

## 1.14.0 / 2020-10-31 / Agent 7.24.0

* [Added] [doc] Add encoding in log config sample. See [#7708](https://github.com/DataDog/integrations-core/pull/7708).

## 1.13.0 / 2020-09-21 / Agent 7.23.0

* [Added] Upgrade psutil to 5.7.2. See [#7395](https://github.com/DataDog/integrations-core/pull/7395).

## 1.12.0 / 2020-08-10 / Agent 7.22.0

* [Added] Add config specs. See [#7258](https://github.com/DataDog/integrations-core/pull/7258).
* [Fixed] Update logs config service field to optional. See [#7209](https://github.com/DataDog/integrations-core/pull/7209).
* [Fixed] Debug logs for failing to retrieve metadata, also add ability to disa…. See [#7255](https://github.com/DataDog/integrations-core/pull/7255).

## 1.11.0 / 2020-05-17 / Agent 7.20.0

* [Added] Allow optional dependency installation for all checks. See [#6589](https://github.com/DataDog/integrations-core/pull/6589).

## 1.10.0 / 2020-04-04 / Agent 7.19.0

* [Added] Upgrade psutil to 5.7.0. See [#6243](https://github.com/DataDog/integrations-core/pull/6243).
* [Fixed] Update deprecated imports. See [#6088](https://github.com/DataDog/integrations-core/pull/6088).
* [Fixed] Remove logs sourcecategory. See [#6121](https://github.com/DataDog/integrations-core/pull/6121).

## 1.9.0 / 2020-01-13 / Agent 7.17.0

* [Added] Use lazy logging format. See [#5377](https://github.com/DataDog/integrations-core/pull/5377).

## 1.8.1 / 2019-12-13 / Agent 7.16.0

* [Fixed] Bump psutil to 5.6.7. See [#5210](https://github.com/DataDog/integrations-core/pull/5210).

## 1.8.0 / 2019-12-02

* [Fixed] Remove shlex. See [#5064](https://github.com/DataDog/integrations-core/pull/5064).
* [Fixed] Upgrade psutil dependency to 5.6.5. See [#5059](https://github.com/DataDog/integrations-core/pull/5059).
* [Added] Add version metadata. See [#4968](https://github.com/DataDog/integrations-core/pull/4968).

## 1.7.2 / 2019-10-11 / Agent 6.15.0

* [Fixed] Upgrade psutil dependency to 5.6.3. See [#4442](https://github.com/DataDog/integrations-core/pull/4442).

## 1.7.1 / 2019-06-06 / Agent 6.12.0

* [Fixed] Fix mac compatibility. See [#3853](https://github.com/DataDog/integrations-core/pull/3853).

## 1.7.0 / 2019-05-14

* [Added] Upgrade psutil dependency to 5.6.2. See [#3684](https://github.com/DataDog/integrations-core/pull/3684).
* [Added] Adhere to code style. See [#3512](https://github.com/DataDog/integrations-core/pull/3512).

## 1.6.0 / 2019-02-18 / Agent 6.10.0

* [Added] Upgrade psutil. See [#3019](https://github.com/DataDog/integrations-core/pull/3019).

## 1.5.0 / 2019-01-04 / Agent 6.9.0

* [Added] Support Python 3. See [#2752][1].

## 1.4.0 / 2018-11-30 / Agent 6.8.0

* [Added] Update psutil. See [#2576][2].

## 1.3.0 / 2018-10-12 / Agent 6.6.0

* [Added] Upgrade psutil. See [#2190][3].

## 1.2.1 / 2018-09-04 / Agent 6.5.0

* [Fixed] Gunicorn intergration - fix problem with multiple master processes. See [#1839][4]. Thanks [mrmm][5].
* [Fixed] Add data files to the wheel package. See [#1727][6].

## 1.2.0 / 2018-03-23

* [FEATURE] add custom tag support.

## 1.1.0 / 2017-05-23

* [BUGFIX] tag all the metrics by app name, not only the service check. See [#414]

## 1.0.0 / 2017-03-22

* [FEATURE] adds gunicorn integration.

<!--- The following link definition list is generated by PimpMyChangelog --->
[1]: https://github.com/DataDog/integrations-core/pull/2752
[2]: https://github.com/DataDog/integrations-core/pull/2576
[3]: https://github.com/DataDog/integrations-core/pull/2190
[4]: https://github.com/DataDog/integrations-core/pull/1839
[5]: https://github.com/mrmm
[6]: https://github.com/DataDog/integrations-core/pull/1727