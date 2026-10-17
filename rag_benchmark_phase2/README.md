
# rag_benchmark Phase 2

## 数据状态
已扫描上传 JSONL：
- Wiki dev
- MuSiQue full train/dev
- MuSiQue ans train/dev
- HotpotQA train/validation

当前 loader 已兼容：
id/question/context 字段。

## 当前阶段
完成：
- Dataset统一接口
- JSONL读取
- Hotpot/MuSiQue/Wiki统一schema
- EM/F1评测
- 实验配置
- UnionGraph Adapter接口占位

未完成：
- 9个baseline官方代码接入
- UnionGraph真实调用入口绑定
- 全量运行

运行:
python run_experiment.py --model uniongraph --dataset musique_ans --limit 1
