
{{- define "chart.list-resources" }}
{{- range $key, $val := .Values.resources }}
  - Effect: 'Allow'
    Action:
      - '{{ $val }}:*'
    Resource:
      - 'arn:aws:{{ $val }}:::*'
{{- end}} 
{{- end}}
