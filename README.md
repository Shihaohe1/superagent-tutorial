# superagent-tutorial

`dsh-superagent` 的新手教程仓库。里面有一个**刻意留下的 bug**，用来演示完整工作流。

## 任务

`src/temperature.py` 的 `c_to_f()` 公式写错了：少了 `+ 32`，所以 `c_to_f(0)` 返回 `0` 而不是 `32`。
`tests/test_temperature.py` 里已经有一条会失败的测试。

请修好 `c_to_f()` 并确保 `python3 -m pytest`（或 `python3 -m unittest`）全绿。
