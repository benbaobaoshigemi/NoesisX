# Writer Identity Handshake And Recovery

`noesisx-push-writer` must verify child role identity before any formal writing work starts.

Use this exact two-line probe right after spawning:

1. `你当前角色名是什么？`
2. `你是否是 writer（是/否）？`

Pass condition:

- role name contains `writer`
- second answer is `是`

Fail condition:

- role name is anything else (for example `Codex`)
- second answer is `否`
- reply is missing, evasive, or mixed with unrelated content

Recovery procedure:

1. Close the failed child agent immediately.
2. Respawn with explicit `agent_type="writer"` and `fork_context=false` (never `true`).
3. Run the same two-line probe again.
4. Retry at most 2 times.
5. If still failing, stop the writer route and report a routing fault to the parent with the probe transcripts.

Guardrails:

- Do not trust nickname, display name, or route label as role proof.
- Do not dispatch deliverable text generation before handshake passes.
- Do not recycle a failed child for writer work.
- Do not use `fork_context=true` in any writer-route spawn or respawn.
