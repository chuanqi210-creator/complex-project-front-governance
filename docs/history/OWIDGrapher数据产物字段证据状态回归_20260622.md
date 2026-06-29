# OWID Grapher 数据产物字段证据状态回归

current_as_of: 2026-06-22

## 1. 小题目标

用 Our World in Data Grapher 的真实图表数据包检验上一轮新增的 `data_artifact_lineage_freshness_guard`：它是否能在真实项目中落地，而不是只停留在字段存在。

选取 artifact：

- chart: `New industrial robots installed per year`
- slug: `annual-industrial-robots-installed`
- CSV: `https://ourworldindata.org/grapher/annual-industrial-robots-installed.csv`
- metadata: `https://ourworldindata.org/grapher/annual-industrial-robots-installed.metadata.json`
- ZIP package: `https://ourworldindata.org/grapher/annual-industrial-robots-installed.zip`
- full metadata: `https://api.ourworldindata.org/v1/indicators/1227958.metadata.json`
- API docs: `https://docs.owid.io/projects/etl/api/chart-api/`

## 2. 实际执行证据

```yaml
micro_task_execution_check:
  task: 下载 OWID Grapher CSV、metadata、ZIP 和 full metadata，实际填写 data_artifact_lineage_freshness_guard
  access_boundary:
    first_attempt: Python urllib default request returned HTTP 403
    fallback: add public User-Agent header and retry read-only public endpoints
    external_write: none
  observed_outputs:
    metadata_json:
      bytes: 2288
      sha256_prefix: 843a9753816fbb58
      top_keys: [chart, columns, dateDownloaded]
    csv:
      bytes: 2104
      sha256_prefix: e859fb7589f26c55
      rows: 83
      header: [Entity, Code, Year, Annual industrial robots installed]
      sample_first_row: [China, CHN, 2011, 23000]
    zip:
      bytes: 3699
      sha256_prefix: 8a9827f5f6d1d852
      files: [annual-industrial-robots-installed.metadata.json, annual-industrial-robots-installed.csv, readme.md]
    full_metadata:
      bytes: 3664
      sha256_prefix: 8b64559b337f2ac8
      top_keys_include: [catalogPath, datasetVersion, dataChecksum, metadataChecksum, origins, processingLevel, updatePeriodDays, updatedAt]
  pass_fail: pass
  exposed_gap: guard 字段能被填写，但若没有 per-field evidence status，会把 unknown/run_id/validation_suite_ref 等缺口误包装成已验证。
```

## 3. 来源角色表

| source | role | can_support | cannot_support |
| --- | --- | --- | --- |
| OWID Grapher CSV | data artifact | 实际图表数据、行数、列名、样本值、下载 hash | 原始生产者证据、完整 ETL run、质量验证结果 |
| OWID Grapher metadata.json | package metadata | dateDownloaded、chart citation、column lastUpdated、nextUpdate、timespan、fullMetadata URL | 完整来源层级、run/job id、测试套件 |
| OWID ZIP readme | package documentation | 下载日期、CSV/metadata 结构说明、重用与引用责任、last updated/next update | 当前质量验证、真实决策用途、完整复现 |
| OWID indicator full metadata | stronger metadata | catalogPath、datasetVersion、dataChecksum、metadataChecksum、processingLevel、origins、updatePeriodDays、updatedAt | 本地 ETL 运行日志、质量测试报告、下游使用安全 |
| OWID Chart API docs | API behavior | `.csv`、`.metadata.json`、`.zip` 等访问方式的官方文档背景 | 不能证明某个具体图表当前质量或语义适用 |
| Stanford AI Index / IFR via AI Index | origin | 原始主题来源和引用链 | OWID minor processing 的所有实现细节 |

## 4. data_artifact_lineage_freshness_guard 实例

```yaml
data_artifact_lineage_freshness_guard:
  artifact_id: owid-grapher/annual-industrial-robots-installed
  artifact_type: chart_data_package
  owner: Our World in Data
  status: active_source_backed
  version:
    datasetVersion: 2026-04-20
    indicator_updatedAt: 2026-05-18T08:39:50.000Z
    dateDownloaded: 2026-06-22
  artifact_path_or_uri:
    csv: https://ourworldindata.org/grapher/annual-industrial-robots-installed.csv
    metadata: https://ourworldindata.org/grapher/annual-industrial-robots-installed.metadata.json
    zip: https://ourworldindata.org/grapher/annual-industrial-robots-installed.zip
    full_metadata: https://api.ourworldindata.org/v1/indicators/1227958.metadata.json
  source_assets:
    - International Federation of Robotics via AI Index Report (2026)
    - AI Index Report, Stanford HAI, published 2026-04-13
  input_versions_or_hashes:
    csv_sha256_prefix: e859fb7589f26c55
    metadata_sha256_prefix: 843a9753816fbb58
    zip_sha256_prefix: 8a9827f5f6d1d852
    full_metadata_sha256_prefix: 8b64559b337f2ac8
    dataChecksum: "8839915782047449179"
    metadataChecksum: "1551085839315423289"
  source_current_as_of:
    lastUpdated: 2026-04-20
    nextUpdate: 2027-04-20
    origin_dateAccessed: 2026-04-20
    origin_datePublished: 2026-04-13
    timespan: 2011-2024
  produced_at_or_refreshed_at:
    package_downloaded: 2026-06-22
    indicator_updatedAt: 2026-05-18T08:39:50.000Z
  code_ref: unknown_in_downloaded_package
  run_id: unknown_in_downloaded_package
  parameters_ref: default public Grapher CSV/metadata/ZIP endpoints
  environment_ref: local Python 3.9 urllib read-only download with User-Agent header
  transformation_logic:
    processingLevel: minor
    citation: International Federation of Robotics via AI Index Report (2026) – with minor processing by Our World in Data
    catalogPath: grapher/artificial_intelligence/2026-04-20/ai_index/industrial_robots#industrial_robot_installations
  lineage_ref:
    fullMetadata: https://api.ourworldindata.org/v1/indicators/1227958.metadata.json
    origin_pdf: https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf
  freshness_policy:
    updatePeriodDays: 365
    nextUpdate: 2027-04-20
  freshness_checked_at: 2026-06-22
  freshness_status: source_backed_fresh_candidate
  validation_suite_ref: unknown_in_public_artifact
  validation_checked_at: unknown
  validation_status: unknown
  artifact_checksum:
    csv_sha256_prefix: e859fb7589f26c55
    full_metadata_dataChecksum: "8839915782047449179"
  reproduction_recipe_ref:
    - download CSV, metadata.json, ZIP and full metadata endpoints with public read-only request
    - verify byte sizes, hashes, row count, header and selected metadata fields
  downstream_references:
    - candidate report/chart citation only
  intended_use:
    - source-backed citation of OWID chart data
  known_caveats:
    - OWID notes it is almost never the original producer of data
    - downloaded package does not expose a validation suite, ETL run id, or complete code execution evidence
    - "minor processing" needs original report review before strong causal or decision claims
  previous_or_superseded_version: unknown_from_public_package
  downgrade_if_stale: if after nextUpdate without refreshed package, or if original source/definition conflicts are unresolved, downgrade to stale_or_source_backed_candidate
```

## 5. 字段证据状态 field_evidence_status

| field_name | evidence_status | evidence_uri_or_hash | extracted_value | gap_action |
| --- | --- | --- | --- | --- |
| artifact_id | direct_observed | CSV/metadata URL | `annual-industrial-robots-installed` | none |
| artifact_type | inferred | ZIP package files | chart data package | mark as inferred |
| owner | direct_observed | OWID URLs/readme | Our World in Data | none |
| datasetVersion | direct_observed | full metadata sha `8b64559b337f2ac8` | `2026-04-20` | none |
| dateDownloaded | direct_observed | package metadata/readme | `2026-06-22` | none |
| input_versions_or_hashes | direct_observed | local download hashes + full metadata | CSV/metadata/ZIP/full metadata hashes; `dataChecksum` | none |
| transformation_logic | derived_from_metadata | full metadata / citation | `processingLevel: minor`; catalogPath | review ETL/code if stronger claim needed |
| run_id | unknown | public package | not exposed | do not claim ETL run reproducibility |
| validation_suite_ref | unknown | public package | not exposed | do not claim quality suite pass |
| validation_status | unknown | public package | not exposed | keep readiness at source-backed/local retrieval |
| freshness_policy | direct_observed | metadata/full metadata | nextUpdate 2027-04-20; updatePeriodDays 365 | none |
| reproduction_recipe_ref | derived_from_metadata | public endpoints + local command evidence | can reproduce retrieval, not full ETL | limit to retrieval reproduction |
| downstream_references | inferred | current regression file | candidate report/chart citation | require downstream review if used in report |

## 6. 共性修正

本轮不新增一个新领域模板，只把 `data_artifact_lineage_freshness_guard` 从“字段清单”升级为“字段证据强度表”。核心修正：

```yaml
rule_update:
  trigger: data_artifact_guard_is_used_on_real_project
  required_behavior:
    - 每个关键字段标注 evidence_status
    - unknown / inferred / derived_from_metadata 不得提升 claim_readiness
    - field_evidence_status 必须写 evidence_uri_or_hash、extracted_value 和 gap_action
  failure_mode: data_artifact_guard_checkbox_gap
  downgrade_rule: guard 模板填满但关键字段为 unknown 时，只能保留 source_backed 或 locally_retrieved，不得写可复现、质量验证通过或可决策。
```

## 7. 下一步

真实项目中的下一轮可进一步测试：含模型 registry、CI、数据版本、论文 benchmark 或 BI dashboard 的项目，是否也会出现“字段看似齐全、证据强度不足”的问题。
