def test_runner_prints_nodes(capfd):
    from executor.dag_runner import run_dag
    run_dag("examples/hello_world.json")
    out, _ = capfd.readouterr()
    assert "task1" in out